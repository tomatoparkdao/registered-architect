# 中国建筑规范图集（DWG）索引

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。

全库结构与入口见 [README.md](README.md)。本页只做链接索引，分两块：全库索引与首测样本。

## 全库

| 入口 | 说明 |
|---|---|
| [../ATLAS_ROUTING.md](../ATLAS_ROUTING.md) | 图集 ↔ 规范双向路由（14 主题 / 83 图册 / 198 编号） |
| [../CODE_RELATIONS.md](../CODE_RELATIONS.md) | 规范互引图谱 |
| [batch/batch_manifest.json](batch/batch_manifest.json) | 批次总清单与分片索引（4351 条源文件记录） |
| [batch/drawings/](batch/drawings/) | 4335 张图的蒸馏产物，一图一目录 |
| [reports/coverage_report.md](reports/coverage_report.md) | 覆盖率：成功 / 无效 / 稳定失败 |
| [reports/dwg_final_failures.md](reports/dwg_final_failures.md) | 稳定失败清单与最终原因 |
| [reports/artifact_size_audit.json](reports/artifact_size_audit.json) | 1 MiB 体积审计 |
| [gpu_execution_report.md](gpu_execution_report.md) | CUDA 阶段与设备信息 |
| [scripts/build_atlas_routing.py](scripts/build_atlas_routing.py) | 重建两张路由表 |

## 首测样本（CN-DETAIL-0001 女儿墙压顶及泛水）

| 内容 | 文件 |
|---|---|
| 来源清单 / 元数据 | [source_inventory.json](source_inventory.json)、[source_metadata.json](source_metadata.json) |
| 几何 / 图层 / 块 | [geometry.json](geometry.json)、[layers.json](layers.json)、[blocks.json](blocks.json) |
| 尺寸 / 文字 | [dimensions.json](dimensions.json)、[text_annotations.json](text_annotations.json) |
| 构造语义 | [semantics.json](semantics.json)、[semantic_index.json](semantic_index.json) |
| 重绘配方与步骤 | [cad_recipe.json](cad_recipe.json)、[source_reconstruction.md](source_reconstruction.md) |
| 重绘验证 | [reconstruction_test_report.md](reconstruction_test_report.md)、[reconstruction/entity_handle_map.json](reconstruction/entity_handle_map.json) |
| 重绘 DXF | [reconstruction/CN-DETAIL-0001-reconstructed.dxf](reconstruction/CN-DETAIL-0001-reconstructed.dxf) |
| 图纸索引 | [drawing_index.json](drawing_index.json) |

---

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
