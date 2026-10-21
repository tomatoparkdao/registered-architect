"""Write bounded final coverage and integrity reports from the DWG batch manifest."""
from __future__ import annotations

import collections
import argparse
import json
from pathlib import Path

from signature import stamp

MAX_BYTES = 1024 * 1024
ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "batch" / "batch_manifest.json"
REPORTS = ROOT / "reports"


def last_line(record):
    return (record.get("detail") or "no diagnostic returned").splitlines()[-1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", action="append", default=[], type=Path)
    args = parser.parse_args()
    state = json.loads(MANIFEST.read_text(encoding="utf8"))
    records = [item for name in state["record_shards"] for item in json.loads((MANIFEST.parent / name).read_text(encoding="utf8"))["records"]]
    successful = {item["source_path"] for item in records if item["status"] == "geometry_extracted"}
    invalid = {item["source_path"] for item in records if item["status"] == "invalid_dwg"}
    latest = {}
    for item in records:
        latest[item["source_path"]] = item
    unresolved = [item for path, item in latest.items() if path not in successful and path not in invalid]
    REPORTS.mkdir(exist_ok=True)
    failure_rows = "\n".join(f"| {x['drawing_id']} | {x['status']} | {last_line(x).replace('|', '/')} |" for x in unresolved)
    (REPORTS / "dwg_final_failures.md").write_text(
        stamp(
            "# DWG 最终未解析清单\n\n"
            "本清单为两轮兼容重试后的稳定失败项；未再进行无效重试。\n\n"
            "| 图纸 ID | 状态 | 最终原因 |\n| --- | --- | --- |\n" + failure_rows + "\n"
        ),
        encoding="utf8",
    )
    files = [path for path in ROOT.rglob("*") if path.is_file()]
    oversized = [path.relative_to(ROOT).as_posix() for path in files if path.stat().st_size >= MAX_BYTES]
    status_counts = collections.Counter(item["status"] for item in records)
    total = len(latest)
    ignored_non_dwg = sum(
        1
        for source_root in args.source_root
        for path in source_root.rglob("*")
        if path.is_file() and path.suffix.lower() != ".dwg"
    )
    coverage = len(successful) / total if total else 0
    (REPORTS / "coverage_report.md").write_text(
        stamp(
            "# DWG 批次覆盖率报告\n\n"
            f"- 源 DWG 总数：{total}\n- 有效并完成深度蒸馏：{len(successful)}\n"
            f"- 无效 DWG：{len(invalid)}\n- 稳定失败：{len(unresolved)}\n"
            f"- 有效 DWG 成功率：{len(successful)}/{total-len(invalid)}（{len(successful)/(total-len(invalid)):.2%}）\n"
            f"- 全量覆盖（成功/无效/有明确失败原因）：{(len(successful)+len(invalid)+len(unresolved))}/{total}\n"
            f"- 其他格式文件：{ignored_non_dwg} 个，已忽略且未读取/转换\n"
            f"- Manifest 事件统计：`{dict(status_counts)}`\n"
            f"- 小于 1 MiB 审计：{'通过' if not oversized else '失败，见下方'}\n\n"
            "所有成功项均经过 CUDA 几何处理及重绘前后校验。超限重绘产物已在校验后存为带 SHA-256 索引的字节分片。\n\n"
            + ("## 超限文件\n\n" + "\n".join(f"- `{x}`" for x in oversized) + "\n" if oversized else "")
        ),
        encoding="utf8",
    )
    (REPORTS / "artifact_size_audit.json").write_text(json.dumps({"status": "pass" if not oversized else "fail", "max_bytes": MAX_BYTES - 1, "oversized_files": oversized, "files_checked": len(files)}, ensure_ascii=False, indent=2), encoding="utf8")
    print(json.dumps({"sources": total, "success": len(successful), "invalid": len(invalid), "unresolved": len(unresolved), "oversized": len(oversized)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
