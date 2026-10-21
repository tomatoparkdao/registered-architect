# DWG 批次覆盖率报告

- 源 DWG 总数：4351
- 有效并完成深度蒸馏：4335
- 无效 DWG：6
- 稳定失败：10
- 有效 DWG 成功率：4335/4345（99.77%）
- 全量覆盖（成功/无效/有明确失败原因）：4351/4351
- 其他格式文件：189 个，已忽略且未读取/转换
- Manifest 事件统计：`{'conversion_failed': 36, 'geometry_extracted': 4335, 'parse_failed': 687, 'invalid_dwg': 6}`
- 小于 1 MiB 审计：失败，见下方

所有成功项均经过 CUDA 几何处理及重绘前后校验。超限重绘产物已在校验后存为带 SHA-256 索引的字节分片。

## 超限文件

- `batch/drawings/0d9deaa05846/blocks_shards/blocks-0033.json`
- `batch/drawings/0d9deaa05846/cad_recipe_shards/cad_recipe-0033.json`
- `batch/drawings/40617a84e09f/blocks_shards/blocks-0002.json`
- `batch/drawings/40617a84e09f/blocks_shards/blocks-0003.json`
- `batch/drawings/40617a84e09f/blocks_shards/blocks-0005.json`
- `batch/drawings/40617a84e09f/blocks_shards/blocks-0007.json`
- `batch/drawings/40617a84e09f/cad_recipe_shards/cad_recipe-0002.json`
- `batch/drawings/40617a84e09f/cad_recipe_shards/cad_recipe-0003.json`
- `batch/drawings/40617a84e09f/cad_recipe_shards/cad_recipe-0005.json`
- `batch/drawings/40617a84e09f/cad_recipe_shards/cad_recipe-0007.json`
- `batch/drawings/eb562b4fabd5/blocks_shards/blocks-0002.json`
- `batch/drawings/eb562b4fabd5/blocks_shards/blocks-0003.json`
- `batch/drawings/eb562b4fabd5/blocks_shards/blocks-0005.json`
- `batch/drawings/eb562b4fabd5/blocks_shards/blocks-0007.json`
- `batch/drawings/eb562b4fabd5/cad_recipe_shards/cad_recipe-0002.json`
- `batch/drawings/eb562b4fabd5/cad_recipe_shards/cad_recipe-0003.json`
- `batch/drawings/eb562b4fabd5/cad_recipe_shards/cad_recipe-0005.json`
- `batch/drawings/eb562b4fabd5/cad_recipe_shards/cad_recipe-0007.json`
