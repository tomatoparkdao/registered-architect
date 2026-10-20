# 中国建筑规范图集（DWG）

本目录是 `country-china` 的新增资料模块，仅收录 DWG 的结构化蒸馏结果；不复制原始 DWG，也不将未验证的图纸内容当作规范条文。

当前首测处理的是“细部构造”中的一个女儿墙节点图。链路为 `DWG → 临时 DXF → ezdxf 实体解析 → CUDA 坐标校验 → CAD Recipe → 重绘 DXF → 对比验证`。临时 DXF 不进入模块；最终保留真实几何、图层、块、文字、尺寸、语义和重绘文件。

入口索引见 [index.md](index.md)，深度蒸馏脚本见 [scripts/deep_distill_dwg.py](scripts/deep_distill_dwg.py)。
