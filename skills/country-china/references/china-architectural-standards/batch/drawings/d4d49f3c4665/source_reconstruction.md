# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`jg.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[1928.7, -7417.63], [5700.0, -2100.0]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `TEXT`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `DL`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `RXD`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `TREE`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `SY`｜源 `- ` → 重绘 `-`
7. `create_layer`｜图层 `ZZW`｜源 `- ` → 重绘 `-`
8. `create_layer`｜图层 `PD`｜源 `- ` → 重绘 `-`
9. `create_layer`｜图层 `WALL1`｜源 `- ` → 重绘 `-`
10. `create_layer`｜图层 `BUILD`｜源 `- ` → 重绘 `-`
11. `create_layer`｜图层 `TREE01`｜源 `- ` → 重绘 `-`
12. `create_layer`｜图层 `W`｜源 `- ` → 重绘 `-`
13. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
14. `insert_block`｜图层 `0`｜源 `E000001 ` → 重绘 `R000001`
15. `draw_line`｜图层 `0`｜源 `E000002 ` → 重绘 `R000002`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
