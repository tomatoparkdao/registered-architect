"""生成「图集 ↔ 规范」双向路由与「规范互引」图谱。

数据来源全部在仓库内，不联网、不推测：

1. `batch/record_shards/*.json` —— 每张 DWG 的源路径与蒸馏状态；
2. `../standards/*.md` 与 `../standards/text/*.md` —— 规范与图集的条文文本；
3. 图纸标题（源文件名）与图册目录名 —— 图纸的主题线索。

关系不是人工指定的，而是两条可复核的统计口径：

- 主题共现：图纸标题命中主题关键词，条文正文命中同一关键词，两侧条数即为权重；
- 标准互引：条文正文里出现其他标准编号，即为一条引用边。

输出（均小于 1 MiB，便于随 Skill 分发）：

- `../atlas-routing.json` / `../ATLAS_ROUTING.md`
- `../code-relations.json` / `../CODE_RELATIONS.md`

重跑命令（在本目录下）：

    python build_atlas_routing.py
"""

from __future__ import annotations

import collections
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from signature import SIG_CN

ROOT = Path(__file__).resolve().parent.parent  # china-architectural-standards/
REFERENCES = ROOT.parent  # references/
STANDARDS = REFERENCES / "standards"
TEXT = STANDARDS / "text"

# 主题词典：顺序即优先级，先命中者为主主题；一份图纸可以有多个主题。
# 刻意不收「节点 / 大样 / 详图」这类通用词——它们会吞掉全部图纸，没有区分力。
TOPICS = [
    ("roof-waterproof", "屋面与防水", ["屋面", "防水", "女儿墙", "天沟", "檐口", "泛水", "卷材", "涂膜", "种植屋面", "瓦屋面", "雨水", "排水"]),
    ("envelope-wall", "墙体与幕墙", ["幕墙", "墙身", "外墙", "隔墙", "保温", "砌体", "干挂", "石材", "铝板", "铝塑板", "轻钢", "玻璃", "压顶", "窗台"]),
    ("floor-ceiling", "楼地面与吊顶", ["地面", "楼面", "地坪", "吊顶", "天花", "踢脚", "散水", "木地板", "防静电", "找平", "架空"]),
    ("opening-component", "门窗与栏杆构件", ["门窗", "门套", "窗套", "栏杆", "栏板", "扶手", "雨棚", "雨篷", "百叶", "花格", "花窗", "门扇", "门洞", "窗洞", "推拉门", "平开门", "防火门", "飘窗"]),
    ("joint-connection", "变形缝与连接件", ["变形缝", "沉降缝", "伸缩缝", "抗震缝", "后浇带", "埋件", "预埋", "收口", "连接件", "锚固", "胀栓"]),
    ("steel-structure", "钢结构与金属构件", ["钢结构", "型钢", "焊缝", "焊接", "螺栓", "铆接", "桁架", "网架", "檩条", "钢梁", "钢柱", "屋架", "钢支撑"]),
    ("civil-defense", "人防与地下工程", ["人防", "防爆", "密闭", "防护门", "掩蔽", "地下室", "地下工程"]),
    ("heritage-classic", "古建与中式欧式构件", ["古建", "中式", "斗拱", "雀替", "木构", "欧式", "罗马", "柱式", "挂落", "宝顶"]),
    ("piping-equipment", "管道与设备安装", ["阀门", "法兰", "管道", "管件", "采暖", "通风", "消防栓", "水泵", "风口", "设备基础"]),
    ("electrical", "电气与弱电", ["电气", "控制", "原理图", "桥架", "配电", "照明", "接线", "图例"]),
    ("interior-finish", "室内装修与饰面", ["木饰面", "软包", "石膏板", "铝扣", "云石", "暖气罩", "踢脚线", "饰面", "隔断", "吸音板", "墙纸"]),
    ("drafting-standard", "制图与图框", ["图框", "制图", "符号", "标题栏", "图纸目录", "设计说明", "线型", "标注"]),
    ("site-landscape", "室外与景观", ["室外", "景观", "树穴", "水体", "铺装", "挡土墙", "道路", "围墙", "室外工程"]),
    ("structure-base", "结构与基础", ["基础", "承台", "桩", "圈梁", "过梁", "构造柱", "楼板", "屋面板"]),
]

TOPIC_ORDER = [tid for tid, _board, _kws in TOPICS]

# 能直接作为合规依据引用的类型；其余（教材、技术措施、条文说明）只作参考。
MAIN_KINDS = {"国家标准", "推荐性国标", "行业标准", "地方标准", "图集"}

# 标准编号：国标 / 行标 / 地方标准 / 国标图集（如 05J804、13J811、15K606）。
CODE_RE = re.compile(
    r"(?<![A-Za-z0-9])((?:GB/T|GB|JGJ/T|JGJ|CJJ/T|CJJ|JG|MH/T|MH|DB\d{2}/?T?)\s*\d{2,5}(?:[-—]\d{4})?"
    r"|\d{2}[A-Z]{1,3}\d{1,4}(?:[-—]\d{1,2})?)(?![0-9])"
)
PREFIX_RE = re.compile(r"^(gb/t|gb|gbt|jgj/t|jgj|jgjt|cjj/t|cjj|cjjt|jg|mh/t|mh|db\d*/?t?)\s*(\d{2,5})$")
# 图集扫描件的文件名形如 supplement-02J503-1-常用建筑色-<hash>.md，
# 只在明确带 supplement 前缀时才取编号——否则会把文件名尾部的哈希误认成图集号。
SUPPLEMENT_RE = re.compile(
    r"^supplement(?:al)?-((?:GB|JGJ|CJJ|JG|MH)\s*/?\s*T?\s*\d{2,5}|\d{2}[A-Z]{1,3}\d{1,4}(?:-\d{1,2})?)-",
    re.I,
)
# 标题里可能写成 GB-50108-2008、CJJT 78-2010 这类变体，统一在这里收口。
LOOSE_RE = re.compile(r"((?:GB|JGJ|CJJ|JG|MH)\s*[-/]?\s*T?\s*\d{2,5})")
# 源文件名笔误：`supplement-GB345-2012-屋面工程技术规范` 与
# `supplement-GB50345-2012屋面工程技术规范` 是同一份文件，前者漏了 `50`。
# 只登记这种「同名文件另有正确编号」的情况，不做猜测性映射。
CODE_ALIASES = {"GB 345": "GB 50345"}
SKIP_NAMES = {"readme.md", "index.md"}
SKIP_TITLE_KEYWORDS = ("源文件清单", "规范清单")
GUIDE_WORDS = ("实施指南", "条文说明", "解读", "辅导教材", "培训教材")
HEAD_RE = re.compile(r"^#\s+(.{0,140})$", re.M)
PAGE_RE = re.compile(r"^##\s+第\s*\d+\s*页", re.M)


def norm_code(value: str) -> str:
    """把编号压成可比较的形式：GB50016-2014 → GB 50016；05j804 → 05J804。"""
    value = value.strip().upper().replace("—", "-").replace("－", "-")
    value = re.sub(r"\s+", "", value)
    value = re.sub(r"^(GB|JGJ|CJJ|JG|MH)[-/]?T(\d)", r"\1/T \2", value)
    value = re.sub(r"^(GB|JGJ|CJJ|JG|MH)(\d)", r"\1 \2", value)
    return re.sub(r"-\d{4}$", "", value)


def kind_of(code: str) -> str:
    if re.match(r"^\d{2}[A-Z]", code):
        return "图集"
    if code.startswith("GB/T"):
        return "推荐性国标"
    if code.startswith("GB"):
        return "国家标准"
    if code.startswith(("JGJ", "CJJ", "JG", "MH")):
        return "行业标准"
    if code.startswith("DB"):
        return "地方标准"
    return "技术文件"


def starts_with_code(title: str, code: str) -> bool:
    """标题是否以该编号开头——合并同编号的多份文件时，用它挑出规范正文那份。"""
    head = norm_code(re.sub(r"^[《〈\s]+", "", title)[: len(code) + 4])
    return head.startswith(code)


def code_from_name(basename: str, title: str) -> tuple[str, bool]:
    """先按文件名前缀判编号（最稳），再退回标题里的编号；都没有就是技术文件。"""
    prefix = basename.split("-")[0].lower().replace("_", "")
    match = PREFIX_RE.match(prefix)
    if match:
        head, number = match.group(1), match.group(2)
        head = {"gbt": "GB/T", "jgjt": "JGJ/T", "cjjt": "CJJ/T"}.get(head, head.upper())
        return CODE_ALIASES.get(f"{head} {number}", f"{head} {number}"), True
    if re.match(r"^\d{2}[a-z]{1,3}\d{1,4}([-]\d{1,2})?$", prefix):
        return prefix.upper(), True
    supplement = SUPPLEMENT_RE.match(basename)
    if supplement:
        code = norm_code(supplement.group(1))
        return CODE_ALIASES.get(code, code), True
    found = CODE_RE.search(title) or LOOSE_RE.search(title)
    if found:
        code = norm_code(found.group(1))
        return CODE_ALIASES.get(code, code), True
    bare = re.match(r"^(\d{5})(?:-\d{4})?", title)
    if bare:
        return f"GB {bare.group(1)}", True
    return title, False


def topic_hits(text: str) -> collections.Counter:
    """统计一段文本对每个主题的命中次数（按关键词出现次数累加）。"""
    hits = collections.Counter()
    for tid, _board, kws in TOPICS:
        total = 0
        for kw in kws:
            total += text.count(kw)
        if total:
            hits[tid] = total
    return hits


def load_drawings():
    """从批次清单恢复图纸索引，按源路径去重，只保留蒸馏成功项。"""
    manifest = json.loads((ROOT / "batch" / "batch_manifest.json").read_text(encoding="utf8"))
    latest = {}
    for name in manifest["record_shards"]:
        for record in json.loads((ROOT / "batch" / name).read_text(encoding="utf8"))["records"]:
            latest[record["source_path"]] = record
    drawings = []
    for path, record in latest.items():
        if record["status"] != "geometry_extracted":
            continue
        parts = path.split("\\")
        unique = record["drawing_id"].split("-")[-1].lower()
        drawings.append(
            {
                "id": record["drawing_id"],
                "dir": unique,
                "relpath": f"batch/drawings/{unique}",
                "collection": parts[9].strip() if len(parts) > 10 else "(根)",
                "title": parts[-1].rsplit(".", 1)[0],
                "folder": parts[-2] if len(parts) > 2 else "",
            }
        )
    drawings.sort(key=lambda item: (item["collection"], item["title"], item["id"]))
    return drawings


def load_standards():
    """读取规范与图集正文，按编号聚合；正文取 text/ 分片，没有分片就退回条目页。"""
    fragments = collections.defaultdict(list)
    for path in sorted(TEXT.glob("*.md")):
        base = re.sub(r"-\d{3}$", "", path.name[:-3])
        fragments[base].append(path)

    entries = {}
    for path in sorted(STANDARDS.glob("*.md")):
        if path.name.lower() in SKIP_NAMES:
            continue
        head = HEAD_RE.search(path.read_text(encoding="utf-8", errors="replace")[:4000])
        if not head:
            continue
        title = head.group(1).strip()
        if any(word in title for word in SKIP_TITLE_KEYWORDS):
            continue
        base = path.name[:-3]
        code, coded = code_from_name(base, title)
        # 图集常有分册：文件名写成 09j202，标题却是「09J202-1 坡屋面…」，
        # 以标题里的分册号为准，避免同一本图集被拆成两个节点。
        if coded and code[:1].isdigit():
            suffix = re.match(re.escape(code) + r"-(\d{1,2})(?!\d)", norm_code(title))
            if suffix:
                code = f"{code}-{suffix.group(1)}"
        # 实施指南、条文说明、解读这类辅导材料与母标准正文分开计，
        # 否则「指南」里的大量复述会把母标准的被引次数与主题密度一起抬高。
        guide = coded and any(word in title for word in GUIDE_WORDS)
        if guide:
            code = f"{code}·说明"
        entry = entries.setdefault(
            code,
            {
                "code": code,
                "title": title,
                "kind": "条文说明" if guide else (kind_of(code) if coded else "技术文件"),
                "coded": coded and not guide,
                "guide": guide,
                "chars": 0,
                "hits": collections.Counter(),
                "mentions": collections.Counter(),
                "fragments": 0,
            },
        )
        bodies = [item.read_text(encoding="utf-8", errors="replace") for item in fragments.get(base, [])]
        if not bodies:
            bodies = [path.read_text(encoding="utf-8", errors="replace")]
        else:
            entry["fragments"] += len(bodies)
            entry["title"] = entry["title"] or title
        # 同一编号有多份文件时，优先保留以编号开头的那份标题，避免留下笔误版本。
        if starts_with_code(title, code.split("·")[0]) and not starts_with_code(entry["title"], code.split("·")[0]):
            entry["title"] = title
        for body in bodies:
            text = PAGE_RE.sub("", body)
            entry["chars"] += len(text)
            entry["hits"].update(topic_hits(text))
            for found in CODE_RE.findall(text):
                other = norm_code(found)
                if other != code:
                    entry["mentions"][other] += 1
    return entries


def build():
    drawings = load_drawings()
    standards = load_standards()

    # 图纸 → 主题（标题 + 图册名 + 上级目录一起看，源目录层级本身带语义）
    topic_drawings = collections.defaultdict(list)
    collections_by_topic = collections.defaultdict(collections.Counter)
    for item in drawings:
        hits = topic_hits(item["collection"] + "/" + item["folder"] + "/" + item["title"])
        ranked = [tid for tid, _ in sorted(hits.items(), key=lambda kv: (-kv[1], TOPIC_ORDER.index(kv[0])))]
        item["topics"] = ranked
        for tid in ranked:
            topic_drawings[tid].append(item)
            collections_by_topic[tid][item["collection"]] += 1

    collection_counts = collections.Counter(item["collection"] for item in drawings)
    collection_topics = collections.defaultdict(collections.Counter)
    for item in drawings:
        for tid in item["topics"]:
            collection_topics[item["collection"]][tid] += 1

    # 主题 → 规范：按「每万字命中数」排序，避免大厚本靠体量盖过专门条文；
    # 规范与图集排前，教材/技术措施/审查解答这类技术文件单列，不混在一起比。
    topic_standards = {}
    for tid in TOPIC_ORDER:
        rows = []
        for code, entry in standards.items():
            hits = entry["hits"][tid]
            if hits < 5 or entry["chars"] < 1500:
                continue
            density = hits / (entry["chars"] / 10000)
            if entry["kind"] not in MAIN_KINDS and density < 8:
                continue
            rows.append({"code": code, "hits": hits, "density": round(density, 1), "title": entry["title"][:60], "kind": entry["kind"]})
        rows.sort(key=lambda row: (-row["density"], -row["hits"]))
        topic_standards[tid] = {
            "codes": [row for row in rows if row["kind"] in MAIN_KINDS][:12],
            "docs": [row for row in rows if row["kind"] not in MAIN_KINDS][:3],
        }

    standard_topics = collections.defaultdict(list)
    for tid, rows in topic_standards.items():
        for row in rows["codes"] + rows["docs"]:
            standard_topics[row["code"]].append({"topic": tid, "hits": row["hits"]})

    edges = []
    for code, entry in standards.items():
        for other, count in entry["mentions"].items():
            if count >= 2 and other in standards:
                edges.append({"from": code, "to": other, "mentions": count})
    edges.sort(key=lambda edge: -edge["mentions"])
    cited = collections.Counter()
    citing = collections.Counter()
    for edge in edges:
        cited[edge["to"]] += edge["mentions"]
        citing[edge["from"]] += edge["mentions"]

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "method": "图纸标题主题命中 + 条文正文主题命中 + 条文标准编号互引；均为本地文本统计，非规范指定关系",
        "drawings_total": len(drawings),
        "drawings_unassigned": sum(1 for item in drawings if not item["topics"]),
        "collections_total": len(collection_counts),
        "standards_total": sum(1 for entry in standards.values() if entry["coded"]),
        "documents_total": len(standards),
        "topics": [
            {
                "id": tid,
                "board": board,
                "keywords": kws,
                "drawings": len(topic_drawings[tid]),
                "collections": [{"name": name, "drawings": count} for name, count in collections_by_topic[tid].most_common()],
                "standards": topic_standards[tid],
                "samples": [{"id": item["id"], "title": item["title"], "dir": item["dir"]} for item in topic_drawings[tid][:8]],
            }
            for tid, board, kws in TOPICS
        ],
        "collections": [
            {
                "name": name,
                "drawings": count,
                "topics": [{"id": tid, "drawings": n} for tid, n in collection_topics[name].most_common(3)],
            }
            for name, count in collection_counts.most_common()
        ],
        "standard_index": {
            code: {
                "title": entry["title"][:80],
                "kind": entry["kind"],
                "coded": entry["coded"],
                "topics": sorted(standard_topics.get(code, []), key=lambda row: -row["hits"])[:5],
                "cited_by": cited[code],
                "cites": citing[code],
            }
            for code, entry in sorted(standards.items())
        },
    }
    (REFERENCES / "atlas-routing.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")

    relations = {
        "generated_at": payload["generated_at"],
        "method": "条文正文中的标准编号匹配，同一对被提及 ≥2 次记一条引用边",
        "nodes": len(standards),
        "coded_nodes": payload["standards_total"],
        "edges": len(edges),
        "top_cited": [
            {"code": code, "mentions": n, "title": standards[code]["title"][:60], "kind": standards[code]["kind"]}
            for code, n in cited.most_common(40)
            if code in standards
        ],
        "top_citing": [
            {"code": code, "mentions": n, "title": standards[code]["title"][:60], "kind": standards[code]["kind"]}
            for code, n in citing.most_common(40)
            if code in standards
        ],
        "edges_detail": edges[:600],
    }
    (REFERENCES / "code-relations.json").write_text(json.dumps(relations, ensure_ascii=False, indent=1), encoding="utf-8")

    render(payload, relations, standards)

    print(
        json.dumps(
            {
                "drawings": len(drawings),
                "unassigned": payload["drawings_unassigned"],
                "collections": len(collection_counts),
                "coded_standards": payload["standards_total"],
                "documents": len(standards),
                "edges": len(edges),
            },
            ensure_ascii=False,
        )
    )
    return payload, relations


def cell(value) -> str:
    """表格单元格：竖线替换成全角，避免撑破 Markdown 表格。"""
    return str(value).replace("|", "／").replace("\n", " ").strip()


def render(payload, relations, standards):
    topics = {topic["id"]: topic for topic in payload["topics"]}
    boards = [(tid, topic["board"]) for tid in TOPIC_ORDER for topic in [topics[tid]]]
    coded = payload["standards_total"]
    docs = payload["documents_total"] - coded

    # ---------- ATLAS_ROUTING.md ----------
    lines = [
        "# 图集 ↔ 规范双向路由",
        "",
        SIG_CN,
        "",
        f"这一册把 {payload['drawings_total']} 张蒸馏图纸、{payload['collections_total']} 本图册与 "
        f"{coded} 个规范编号放在同一张网上：从条文反查做法图，或从做法图反查条文，两边都能走通。"
        "关系全部由仓库内文本统计得出，不联网、不引用外部目录。",
        "",
        "## 一、先看该走哪条路径",
        "",
        "| 你手上有什么 | 先查哪张表 | 拿到什么 | 下一步 |",
        "|---|---|---|---|",
        "| 一条规范编号（如 GB 50345） | 第五节「反向检索」 | 该规范覆盖的主题、被引次数 | 顺着主题去第三节拿图册与图号 |",
        "| 一个做法问题（如女儿墙泛水） | 第二节「主题总表」 | 该主题的图册分布与对应规范 | 进第三节看具体图册与图号 |",
        "| 一本图册名（如 14J206） | 第四节「图册全量清单」 | 图数、主主题、目录入口 | 按目录直取 `batch/drawings/<dir>/` |",
        "| 两张图纸做法冲突 | 第五节 + 第六节 | 各自对应的规范与互引链 | 以条文为准，图集只作做法参考 |",
        "",
        "## 二、主题总表：图纸与条文在同一行",
        "",
        "| # | 主题 | 图纸数 | 主图册（前二） | 对应规范（按条文密度） | 补充资料 |",
        "|---|---|---|---|---|---|",
    ]
    for index, (tid, board) in enumerate(boards, 1):
        topic = topics[tid]
        cols = "、".join(f"`{cell(row['name'])}`（{row['drawings']}）" for row in topic["collections"][:2]) or "—"
        codes = "、".join(f"`{row['code']}`" for row in topic["standards"]["codes"][:3]) or "—"
        refs = "、".join(cell(row["code"]) for row in topic["standards"]["docs"][:1]) or "—"
        lines.append(f"| {index} | **{board}** | {topic['drawings']} | {cols} | {codes} | {refs} |")

    lines += ["", "## 三、主题逐条：每类问题该翻哪本图册、核哪条规范", ""]
    for tid, board in boards:
        topic = topics[tid]
        lines += [
            f"### {board}（{topic['drawings']} 张图）",
            "",
            f"识别词：{'、'.join(topic['keywords'][:10])}",
            "",
            "| 图册 | 该主题图数 | 在该图册里的入口 |",
            "|---|---|---|",
        ]
        for row in topic["collections"][:10]:
            lines.append(f"| {cell(row['name'])} | {row['drawings']} | `batch/drawings/` 下按图册名检索 |")
        if len(topic["collections"]) > 10:
            lines.append(f"| 其余 {len(topic['collections']) - 10} 本 | {sum(r['drawings'] for r in topic['collections'][10:])} | 见 `atlas-routing.json` |")
        lines += ["", "| 规范 / 图集编号 | 名称 | 类型 | 主题命中 | 密度（次/万字） |", "|---|---|---|---|---|"]
        for row in topic["standards"]["codes"]:
            lines.append(f"| `{row['code']}` | {cell(row['title'])} | {row['kind']} | {row['hits']} | {row['density']} |")
        if not topic["standards"]["codes"]:
            lines.append("| — | 本地资料未覆盖到该主题的条文 | — | — | — |")
        if topic["standards"]["docs"]:
            lines += ["", "| 技术文件（非强制，仅作参考） | 主题命中 |", "|---|---|"]
            for row in topic["standards"]["docs"]:
                lines.append(f"| {cell(row['code'])} | {row['hits']} |")
        if topic["samples"]:
            lines += ["", "取图示例：" + "、".join(f"`{cell(s['id'])}`（{cell(s['title'])}）" for s in topic["samples"][:4]), ""]
        lines.append("")

    lines += [
        "## 四、图册全量清单",
        "",
        f"{payload['collections_total']} 本图册全部登记在此；`图纸数` 为该图册内蒸馏成功的图纸数量，目录为 `batch/drawings/<dir>/`。",
        "",
        "| 图册 | 图纸数 | 主主题 | 次主题 |",
        "|---|---|---|---|",
    ]
    for row in payload["collections"]:
        first = "、".join(topics[item["id"]]["board"] for item in row["topics"][:1]) or "未归类"
        second = "、".join(topics[item["id"]]["board"] for item in row["topics"][1:2]) or "—"
        lines.append(f"| {cell(row['name'])} | {row['drawings']} | {first} | {second} |")

    lines += [
        "",
        "## 五、反向检索：先有规范，后找图",
        "",
        f"共 {coded} 个规范编号。`被引` 为该编号在其他条文里被提到的次数，`相关主题` 由主题密度倒推，两者都只是检索线索。",
        "",
        "| 规范 / 图集编号 | 名称 | 类型 | 被引 | 相关主题 |",
        "|---|---|---|---|---|",
    ]
    reverse = []
    for code, entry in payload["standard_index"].items():
        if not entry["coded"]:
            continue
        reverse.append((entry["cited_by"], code, entry))
    reverse.sort(key=lambda item: (-item[0], item[1]))
    for cited_by, code, entry in reverse:
        tp = "、".join(f"{topics[row['topic']]['board']}（{row['hits']}）" for row in entry["topics"][:3]) or "—"
        lines.append(f"| `{code}` | {cell(entry['title'])} | {entry['kind']} | {cited_by or '—'} | {tp} |")

    lines += [
        "",
        "## 六、使用规约与边界",
        "",
        "| 项 | 规则 | 为什么 |",
        "|---|---|---|",
        "| 图集的法律地位 | 图集与 CAD 大样是做法参考，不是强制性条文 | 报审只认现行强制性标准；图集讲的是怎么画，不是必须这么画 |",
        "| 主题命中数 | 只代表关键词在两侧同时出现，不等于规范指定了这张图 | 它是检索权重，不是合规结论 |",
        "| 引用方式 | 结论写「按 GB ×××× 第 × 条核对」，图集只作为做法出处附后 | 责任落在条文上，图集无法承担签章责任 |",
        "| 版本状态 | 图集编号可对应多个年份版本，取用前核现行版 | 同一编号不同年份做法会变 |",
        "| 未归类图纸 | `未归类` 的图纸目录名不含主题词，只能按图册整体定位 | 不做猜测性归类，避免把做法张冠李戴 |",
        "| 重跑 | 新增批次后执行 `scripts/build_atlas_routing.py`，两张表同步更新 | 索引是派生数据，不手改 |",
        "",
        "## 七、覆盖率与重跑",
        "",
        "| 指标 | 数值 | 说明 |",
        "|---|---|---|",
        f"| 蒸馏图纸 | {payload['drawings_total']} 张 | 只统计 `geometry_extracted` 的成功项 |",
        f"| 已归入主题 | {payload['drawings_total'] - payload['drawings_unassigned']} 张 | 标题或目录命中主题词 |",
        f"| 未归类 | {payload['drawings_unassigned']} 张 | 纯编号图名（如 `FH01N010`），靠图册定位 |",
        f"| 图册 | {payload['collections_total']} 本 | 源目录的图册层 |",
        f"| 规范编号 | {coded} 个 | 另有 {docs} 份技术文件（教材、技术措施、审查解答）不计入编号 |",
        "",
        "重跑命令（在 `scripts/` 下）：`python build_atlas_routing.py`。",
        "",
        "---",
        "",
        SIG_CN,
        "",
    ]
    (REFERENCES / "ATLAS_ROUTING.md").write_text("\n".join(lines), encoding="utf-8")

    # ---------- CODE_RELATIONS.md ----------
    rel = [
        "# 规范互引图谱",
        "",
        SIG_CN,
        "",
        f"条文里写着「应符合 ×××× 的规定」时，那条线就是下一条要查的地方。本册把 {relations['nodes']} 份文本之间的"
        f" {relations['edges']} 条引用边摊开：谁被引最多、谁引别人最多、哪些成对关系最紧。",
        "",
        "## 一、口径",
        "",
        "| 项 | 说明 |",
        "|---|---|",
        "| 节点 | 本地 `standards/` 下的规范、图集与技术文件，按编号归并 |",
        "| 边 | A 的正文里出现 B 的编号，累计 ≥2 次记一条 A → B 的边 |",
        "| 权重 | 出现次数，不是条文数量，也不是法律效力 |",
        "| 不做什么 | 不判断「谁取代谁」「谁优先」，这类结论只能看现行强制性标准与主管部门文件 |",
        "",
        "## 二、被引最多：绕过它就很难往下走",
        "",
        "| # | 编号 | 名称 | 类型 | 被引次数 |",
        "|---|---|---|---|---|",
    ]
    for index, row in enumerate(relations["top_cited"][:30], 1):
        rel.append(f"| {index} | `{row['code']}` | {cell(row['title'])} | {row['kind']} | {row['mentions']} |")
    rel += [
        "",
        "## 三、引用别人最多：这些文件是「总纲型」入口",
        "",
        "| # | 编号 | 名称 | 类型 | 引用外链次数 |",
        "|---|---|---|---|---|",
    ]
    for index, row in enumerate(relations["top_citing"][:30], 1):
        rel.append(f"| {index} | `{row['code']}` | {cell(row['title'])} | {row['kind']} | {row['mentions']} |")
    rel += [
        "",
        "## 四、最紧的成对关系",
        "",
        "| 引用方 | 被引方 | 次数 | 怎么用 |",
        "|---|---|---|---|",
    ]
    for edge in relations["edges_detail"][:40]:
        rel.append(f"| `{edge['from']}` | `{edge['to']}` | {edge['mentions']} | 查 {edge['from']} 时同步打开 {edge['to']} |")
    rel += [
        "",
        "## 五、怎么用这张网",
        "",
        "| 场景 | 动作 |",
        "|---|---|",
        "| 只拿到一条条文 | 先查第二节，看它引了谁；被引方往往才是操作性条款 |",
        "| 两条规范说法不一致 | 查第四节看两者是否互相引用；互引说明同层，未互引多半是不同层级 |",
        "| 想做做法图 | 回到 `ATLAS_ROUTING.md` 第五节，按规范找主题，再按主题找图册 |",
        "| 新增规范 | 无需改本表，重跑 `build_atlas_routing.py` 即可重新计算边 |",
        "",
        "## 六、边界",
        "",
        "- 引用次数高只说明该文件被频繁提及，**不证明它在法律上优先**；强制性通用规范、项目所在地地方标准、主管部门解释都可能在它之上。",
        "- 本地文本来自公开资料的整理与分片，版本年份必须回官方渠道复核后才可写入合规结论。",
        "- 图集与教材之间的互引只作检索线索，不能当作条文依据。",
        "",
        "---",
        "",
        SIG_CN,
        "",
    ]
    (REFERENCES / "CODE_RELATIONS.md").write_text("\n".join(rel), encoding="utf-8")


if __name__ == "__main__":
    build()
