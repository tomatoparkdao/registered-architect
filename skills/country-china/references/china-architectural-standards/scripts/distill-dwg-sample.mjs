import { mkdir, readFile, stat, writeFile } from "node:fs/promises";
import { basename, relative, resolve } from "node:path";

const MAX_BYTES = 1024 * 1024;
const WARN_BYTES = 800 * 1024;
const [sourcePath, outputPath] = process.argv.slice(2);

if (!sourcePath || !outputPath) {
  throw new Error("用法: node distill-dwg-sample.mjs <源DWG绝对路径> <输出模块目录>");
}

const source = resolve(sourcePath);
const output = resolve(outputPath);
const dirs = ["sheets", "semantics", "schedules", "references", "reports"];
await Promise.all(dirs.map((dir) => mkdir(resolve(output, dir), { recursive: true })));

const sourceStat = await stat(source);
const header = await readFile(source, { encoding: null }).then((data) => data.subarray(0, 6).toString("ascii"));
const version = { AC1014: "AutoCAD R14" }[header] ?? "未知/未支持";
const drawingId = "CN-DETAIL-0001";
const sourceRelativePath = relative(resolve(source, "..", "..", "..", "..", "..", "..", ".."), source).replaceAll("\\", "/");
const sourceName = basename(source);

// 仅依据文件名和目录做来源分类；绝不据此推断尺寸、材料、图层或实体。
const semantic = {
  id: "CN-DETAIL-0001-SEM-001",
  module: "中国建筑规范图集/细部构造",
  source_dwg: drawingId,
  source_layer: null,
  source_block_or_entity_type: null,
  drawing_number: null,
  semantic_category: "女儿墙/压顶/泛水（来源文件名分类，待复核）",
  title: "女儿墙压顶及泛水",
  architectural_description: "文件名表明该图纸涉及女儿墙压顶及泛水节点；当前环境仅完成 DWG 头部识别，尚未提取图内实体、尺寸、材料层次或标高。",
  geometry_summary: "未解析",
  key_dimensions: [],
  material_or_construction_layers: [],
  applicable_scenarios: ["待人工复核：屋面女儿墙节点"],
  usage_limits: "不得作为规范条文、构造尺寸或施工依据；须完成 DWG 转 DXF 后复核。",
  related_entries: [],
  parse_confidence: "low",
  requires_human_review: true
};
const inventory = {
  generated_at: new Date().toISOString(),
  drawings: [{
    drawing_id: drawingId,
    original_filename: sourceName,
    original_absolute_path: source,
    source_relative_path: sourceRelativePath,
    category: "detail_construction",
    file_size_bytes: sourceStat.size,
    modified_at: sourceStat.mtime.toISOString(),
    dwg_header: header,
    dwg_version: version,
    layer_count: null,
    entity_count: null,
    extents: null,
    units: null,
    origin: null,
    parse_status: "partial_metadata_only",
    parser_note: "未检测到可用的 DWG→DXF 转换器或 DXF 解析器；未读取实体、图层和块信息。"
  }]
};
const drawingIndex = { drawings: [{ drawing_id: drawingId, title: "女儿墙压顶及泛水", category: "detail_construction", source_inventory: "source_inventory.json", semantic_files: ["semantics/CN-DETAIL-0001.json"] }] };
const semanticIndex = { entries: [{ id: semantic.id, title: semantic.title, category: semantic.semantic_category, file: "semantics/CN-DETAIL-0001.json", parse_confidence: semantic.parse_confidence }] };
const manifest = { module: "中国建筑规范图集", scope: "DWG 首测", drawing_count: 1, successful: 0, partial: 1, failed: 0, semantic_entry_count: 1, files: ["source_inventory.json", "drawing_index.json", "semantic_index.json", "semantics/CN-DETAIL-0001.json"] };

async function writeJson(path, value) {
  const content = JSON.stringify(value, null, 0);
  if (Buffer.byteLength(content) >= MAX_BYTES) throw new Error(`拒绝写入超限文件: ${path}`);
  await writeFile(path, content, "utf8");
}

await writeJson(resolve(output, "source_inventory.json"), inventory);
await writeJson(resolve(output, "drawing_index.json"), drawingIndex);
await writeJson(resolve(output, "semantic_index.json"), semanticIndex);
await writeJson(resolve(output, "manifest.json"), manifest);
await writeJson(resolve(output, "semantics", "CN-DETAIL-0001.json"), { source_file: drawingId, part_id: 1, total_parts: 1, split_strategy: "not_required", record_count: 1, records: [semantic] });
await writeFile(resolve(output, "reports", "parse_failures.log"), `${drawingId}\tpartial_metadata_only\tDWG ${header} (${version}); no DWG-to-DXF converter or DXF parser available.\n`, "utf8");
await writeFile(resolve(output, "reports", "oversized_files.log"), "No oversized files detected.\n", "utf8");
const report = `# DWG 首测覆盖率报告\n\n- DWG 总数：1\n- 成功解析：0\n- 部分解析：1\n- 失败：0\n- 语义条目：1\n- 图纸索引：1\n- 超大文件：否\n- 人工复核：需要\n\n| 图纸 ID | 原始文件 | DWG 版本 | 状态 |\n| --- | --- | --- | --- |\n| ${drawingId} | ${sourceName} | ${version} | partial_metadata_only |\n\n未检测到可用 DWG 转换/解析工具，因此未生成任何实体、图层、块、尺寸或材料数据。\n`;
await writeFile(resolve(output, "reports", "coverage_report.md"), report, "utf8");
const index = `# 中国建筑规范图集（DWG 首测）\n\n- [来源清单](source_inventory.json)\n- [图纸索引](drawing_index.json)\n- [语义索引](semantic_index.json)\n- [覆盖率报告](reports/coverage_report.md)\n`;
await writeFile(resolve(output, "index.md"), index, "utf8");

const auditPaths = ["README.md", "index.md", "manifest.json", "source_inventory.json", "drawing_index.json", "semantic_index.json", "semantics/CN-DETAIL-0001.json", "reports/parse_failures.log", "reports/oversized_files.log", "reports/coverage_report.md"];
const audit = await Promise.all(auditPaths.map(async (path) => ({ path, size_bytes: (await stat(resolve(output, path))).size })));
const warnings = audit.filter((item) => item.size_bytes >= WARN_BYTES);
if (audit.some((item) => item.size_bytes >= MAX_BYTES)) throw new Error("体积审计失败：存在达到 1024KB 的文件");
await writeFile(resolve(output, "reports", "size_audit.json"), JSON.stringify({ status: warnings.length ? "warning" : "pass", max_bytes: MAX_BYTES, files: audit }, null, 0), "utf8");
console.log(JSON.stringify({ status: "partial", drawing_id: drawingId, version, files_audited: audit.length, warnings: warnings.length }));
