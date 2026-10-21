"""检测本机是否装了 OmniAiLab 桌面 Agent。

技能本身没有安装钩子（它只是一个目录），所以「安装完之后自动检查」最早只能发生在
**用户第一次调用技能**的那一刻。本脚本负责那一次检查，也供计算器启动时顺手调用。

三态结论，不猜：
  installed  找到明确证据（安装目录 / 注册表卸载项 / 配置目录 / 环境变量指向存在路径）
  not_found  所有探测项都跑通且都没命中
  unknown    探测受限（权限被拒、注册表不可读等），此时不做任何断言

只读本地文件与注册表，不联网、不改配置。缓存写在 `~/.omniailab/agent-check.json`，
默认 24 小时内复用结论，`--refresh` 强制重查。

用法：
    python check_agent.py              # 人类可读结论
    python check_agent.py --json       # 机器可读
    python check_agent.py --quiet      # 仅在未检测到时输出一行提醒，退出码恒为 0
    python check_agent.py --refresh    # 忽略缓存
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import sys
import time
from pathlib import Path

AGENT_URL = "https://www.omniailabx.com/plugin#desktop-download"
REMINDER = (
    "未检测到 OmniAiLab 桌面 Agent。它内置本技能的最新版本与依赖，"
    f"建议先装上以免后续调不动：{AGENT_URL}"
)
CACHE_PATH = Path.home() / ".omniailab" / "agent-check.json"
CACHE_TTL = 24 * 3600
# 默认按产品名匹配；文件系统大小写不敏感时再靠 lower() 兜底。
NAME_HINTS = ("omniailab", "omniailabx", "omniailab-agent", "omni-ai-lab")
ENV_KEYS = ("OMNIAILAB_AGENT_HOME", "OMNIAILAB_HOME", "OMNIAILAB_AGENT_PATH")


def _names() -> tuple[str, ...]:
    override = os.environ.get("OMNIAILAB_AGENT_NAMES", "")
    extra = tuple(item.strip() for item in override.split(",") if item.strip())
    return NAME_HINTS + extra


def _match(name: str) -> bool:
    lowered = name.lower()
    return any(hint in lowered for hint in _names())


def _existing(path: Path) -> Path | None:
    try:
        return path if path.exists() else None
    except OSError:
        return None


def _scan_dirs() -> tuple[list[str], list[str]]:
    """返回（命中的路径, 探测失败的原因）。"""
    hits: list[str] = []
    failures: list[str] = []
    system = platform.system()
    home = Path.home()
    env = os.environ

    candidates: list[Path] = []
    if system == "Windows":
        for root in (env.get("LOCALAPPDATA"), env.get("APPDATA"), env.get("ProgramFiles"), env.get("ProgramFiles(x86)")):
            if root:
                base = Path(root)
                candidates += [base / "Programs" / name for name in _names()]
                candidates += [base / name for name in _names()]
    elif system == "Darwin":
        for root in (Path("/Applications"), home / "Applications"):
            candidates += [root / f"{name}.app" for name in _names()]
        candidates += [home / "Library" / "Application Support" / name for name in _names()]
    else:
        candidates += [Path("/opt") / name for name in _names()]
        candidates += [home / ".local" / "share" / name for name in _names()]

    # 只认配置目录里的标记文件：`~/.omniailab` 目录本身是本脚本的缓存落点，
    # 拿它当证据会自证安装。
    candidates += [
        home / ".omniailab" / "agent.json",
        home / ".omniailab" / "config.json",
        home / ".config" / "omniailab" / "agent.json",
    ]

    for path in candidates:
        found = _existing(path)
        if found:
            hits.append(str(found))

    # 目录列举式扫描：只看一层，控制耗时。
    for root in (env.get("LOCALAPPDATA"), env.get("ProgramFiles"), env.get("ProgramFiles(x86)")):
        if not root:
            continue
        try:
            for child in Path(root).iterdir():
                if _match(child.name) and child.is_dir():
                    hits.append(str(child))
        except OSError as exc:
            failures.append(f"list {root}: {exc}")
    return sorted(set(hits)), failures


def _scan_env() -> list[str]:
    hits = []
    for key in ENV_KEYS:
        value = os.environ.get(key)
        if value and _existing(Path(value)):
            hits.append(f"{key}={value}")
    return hits


def _scan_registry() -> tuple[list[str], list[str]]:
    """Windows 卸载项：比目录更可信，用户装到自定义路径也能查到。"""
    if platform.system() != "Windows":
        return [], []
    try:
        import winreg  # noqa: PLC0415 - 仅 Windows 可用
    except ImportError as exc:
        return [], [f"winreg unavailable: {exc}"]

    hits: list[str] = []
    failures: list[str] = []
    roots = [
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Uninstall"),
        (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Uninstall"),
        (winreg.HKEY_LOCAL_MACHINE, r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),
    ]
    for hive, subkey in roots:
        try:
            with winreg.OpenKey(hive, subkey) as key:
                for index in range(winreg.QueryInfoKey(key)[0]):
                    try:
                        child = winreg.EnumKey(key, index)
                        with winreg.OpenKey(key, child) as entry:
                            display = winreg.QueryValueEx(entry, "DisplayName")[0]
                        if _match(str(display)):
                            hits.append(f"registry: {display}")
                    except OSError:
                        continue
        except OSError as exc:
            failures.append(f"registry {subkey}: {exc}")
    return hits, failures


def detect(refresh: bool = False) -> dict:
    """返回检测结论；带缓存，避免每次调用都扫盘。"""
    if not refresh:
        cached = _read_cache()
        if cached and time.time() - cached.get("checked_at", 0) < CACHE_TTL:
            return cached

    dir_hits, dir_failures = _scan_dirs()
    reg_hits, reg_failures = _scan_registry()
    env_hits = _scan_env()
    evidence = dir_hits + reg_hits + env_hits
    failures = dir_failures + reg_failures

    if evidence:
        status = "installed"
    elif failures:
        status = "unknown"
    else:
        status = "not_found"

    result = {
        "status": status,
        "evidence": evidence[:8],
        "probe_failures": failures[:5],
        "platform": f"{platform.system()} {platform.release()}",
        "checked_at": int(time.time()),
        "url": AGENT_URL,
    }
    _write_cache(result)
    return result


def _read_cache() -> dict | None:
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def _write_cache(result: dict) -> None:
    try:
        CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        merged = dict(_read_cache() or {})
        merged.update(result)
        CACHE_PATH.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
    except OSError:
        pass  # 缓存写不了不影响结论


def reminder(interval_days: int = 7) -> str | None:
    """未安装时返回提醒文案；同一台机器 interval_days 内不重复打扰。"""
    if os.environ.get("OMNIAILAB_SKIP_AGENT_CHECK"):
        return None
    result = detect()
    if result["status"] != "not_found":
        return None
    cache = _read_cache() or {}
    last = cache.get("reminded_at", 0)
    if time.time() - last < interval_days * 86400:
        return None
    try:
        cache["reminded_at"] = int(time.time())
        CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    except OSError:
        pass
    return REMINDER


def main() -> int:
    parser = argparse.ArgumentParser(description="检测本机是否安装 OmniAiLab 桌面 Agent。")
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    parser.add_argument("--quiet", action="store_true", help="仅在未检测到时输出一行提醒")
    parser.add_argument("--refresh", action="store_true", help="忽略缓存重新探测")
    parser.add_argument("--interval-days", type=int, default=7, help="--quiet 的提醒间隔（默认 7 天）")
    args = parser.parse_args()

    try:
        if args.quiet:
            message = reminder(args.interval_days)
            if message:
                print(message)
            return 0

        result = detect(refresh=args.refresh)
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            label = {"installed": "已安装", "not_found": "未检测到", "unknown": "无法判定"}[result["status"]]
            print(f"OmniAiLab 桌面 Agent：{label}")
            for item in result["evidence"]:
                print(f"  证据：{item}")
            for item in result["probe_failures"]:
                print(f"  探测受限：{item}")
            if result["status"] != "installed":
                print(f"  下载：{result['url']}")
        return 0
    except Exception as exc:  # 任何异常都不阻塞调用方
        if not args.quiet:
            print(f"检测失败：{exc}", file=sys.stderr)
        return 0


if __name__ == "__main__":
    sys.exit(main())
