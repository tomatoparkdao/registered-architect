# 源图重绘配方

- 源 DWG：`27_墙外双扇推拉门-侧.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[13438.69, 18618.25], [13443.87, 18633.34]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `PUB_DIM`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
4. `draw_polyline`｜图层 `PUB_DIM`｜源 `E000001 ` → 重绘 `R000001`
5. `draw_polyline`｜图层 `0`｜源 `E000002 ` → 重绘 `R000002`
6. `draw_polyline`｜图层 `0`｜源 `E000003 ` → 重绘 `R000003`
7. `draw_line`｜图层 `PUB_DIM`｜源 `E000004 ` → 重绘 `R000004`
8. `draw_line`｜图层 `PUB_DIM`｜源 `E000005 ` → 重绘 `R000005`
9. `draw_line`｜图层 `PUB_DIM`｜源 `E000006 ` → 重绘 `R000006`
10. `draw_line`｜图层 `PUB_DIM`｜源 `E000007 ` → 重绘 `R000007`
11. `draw_line`｜图层 `PUB_DIM`｜源 `E000008 ` → 重绘 `R000008`
12. `draw_line`｜图层 `PUB_DIM`｜源 `E000009 ` → 重绘 `R000009`
13. `draw_line`｜图层 `PUB_DIM`｜源 `E000010 ` → 重绘 `R000010`
