# DWG 批次覆盖率报告

- 源 DWG 总数：4351
- 有效并完成深度蒸馏：4316
- 无效 DWG：6
- 稳定失败：29
- 有效 DWG 成功率：4316/4345（99.33%）
- 全量覆盖（成功/无效/有明确失败原因）：4351/4351
- Manifest 事件统计：`{'conversion_failed': 36, 'geometry_extracted': 4316, 'parse_failed': 675, 'invalid_dwg': 6}`
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
- `batch/drawings/599db96fb0d7/reconstruction/CN-DWG-599DB96FB0D7-reconstructed.dxf`
- `batch/drawings/9eff52d8daf4/reconstruction/CN-DWG-9EFF52D8DAF4-reconstructed.dxf`
- `batch/drawings/d68ae4d27348/reconstruction/CN-DWG-D68AE4D27348-reconstructed.dxf`
- `batch/drawings/eb562b4fabd5/blocks_shards/blocks-0002.json`
- `batch/drawings/eb562b4fabd5/blocks_shards/blocks-0003.json`
- `batch/drawings/eb562b4fabd5/blocks_shards/blocks-0005.json`
- `batch/drawings/eb562b4fabd5/blocks_shards/blocks-0007.json`
- `batch/drawings/eb562b4fabd5/cad_recipe_shards/cad_recipe-0002.json`
- `batch/drawings/eb562b4fabd5/cad_recipe_shards/cad_recipe-0003.json`
- `batch/drawings/eb562b4fabd5/cad_recipe_shards/cad_recipe-0005.json`
- `batch/drawings/eb562b4fabd5/cad_recipe_shards/cad_recipe-0007.json`
