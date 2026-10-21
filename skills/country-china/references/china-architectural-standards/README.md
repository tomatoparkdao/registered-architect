# 中国建筑规范图集（DWG 蒸馏）

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。

本目录是 `country-china` 的图纸资料模块，收录「细部构造 / 设计院通用大样图节点详图」这批 DWG 的结构化蒸馏结果。不复制原始 DWG，也不把未验证的图纸内容当作规范条文。

| 指标 | 数值 | 说明 |
|---|---|---|
| 源 DWG | 4351 份 | 扫描目录后逐份处理，其他格式 189 个已忽略且未读取 |
| 深度蒸馏成功 | 4335 份 | 成功率 99.77%（无效 DWG 6 份、稳定失败 10 份，原因逐条记录） |
| 图册 | 83 本 | 源目录的图册层，见 [../ATLAS_ROUTING.md](../ATLAS_ROUTING.md) 第四节 |
| 单图产物 | 约 20 个文件 | 几何、图层、块、尺寸、文字标注、语义、配方、重绘 DXF 与三份报告 |

## 链路

```
DWG → 临时 DXF → ezdxf 实体解析 → CUDA 坐标校验 → CAD Recipe → 重绘 DXF → 对比验证
```

临时 DXF 不进入模块；保留的是真实几何、图层、块定义、尺寸、文字、构造语义、重绘配方与验证报告。每张图的产物在 `batch/drawings/<dir>/`，`<dir>` 为图号的十二位十六进制部分。

| 文件 | 内容 |
|---|---|
| `geometry.json` | 模型空间实体与坐标（CUDA 校验） |
| `layers.json` / `blocks.json` | 图层表与块定义 |
| `dimensions.json` / `text_annotations.json` | 尺寸标注与文字，构造语义的原始证据 |
| `semantics.json` | 构件、材料、厚度、剖切方向的判断及 `requires_manual_review` 标记 |
| `cad_recipe.json` | 可独立执行的重绘步骤，每步带源/重绘句柄 |
| `reconstruction/` | 重绘 DXF 与逐实体句柄映射 |
| `source_reconstruction.md` / `parse_report.md` / `reconstruction_test_report.md` | 重绘步骤、解析报告与前后对比报告 |

## 两个入口

| 想做什么 | 去哪 |
|---|---|
| 按主题或规范编号找做法图 | [../ATLAS_ROUTING.md](../ATLAS_ROUTING.md)（机读版 `atlas-routing.json`） |
| 判断两条规范的关系 | [../CODE_RELATIONS.md](../CODE_RELATIONS.md)（机读版 `code-relations.json`） |
| 看链接清单 | [index.md](index.md) |
| 看覆盖率与失败项 | [reports/coverage_report.md](reports/coverage_report.md)、[reports/dwg_final_failures.md](reports/dwg_final_failures.md) |
| 重跑蒸馏 | [scripts/deep_distill_dwg.py](scripts/deep_distill_dwg.py)、[scripts/batch_distill_dwg.py](scripts/batch_distill_dwg.py) |
| 重建路由索引 | [scripts/build_atlas_routing.py](scripts/build_atlas_routing.py) |

## 边界

| 项 | 规则 |
|---|---|
| 法律地位 | 图纸是做法参考，不是强制性条文；不得用图纸替代条文结论 |
| 材料与厚度 | 除源图明确标注外一律标 `not_marked_in_source`，不做自动脑补 |
| 构造语义 | 标注 `requires_manual_review` 的项必须人工确认后才能进设计文件 |
| 版本 | 图册编号对应多个年份版本，取用前核现行版；分册号不得省略 |
| 尺寸依据 | 重绘 DXF 用于对照做法，不作报建或加工依据 |

---

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
