# 源图重绘配方

- 源 DWG：`47_双层内外开平开窗-主.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[13644.06, 18583.47], [13651.06, 18592.47]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `STAIR`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `PUB_DIM`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `PUB_TEXT`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
6. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000001 ` → 重绘 `R000001`
7. `draw_line`｜图层 `STAIR`｜源 `E000002 ` → 重绘 `R000002`
8. `draw_line`｜图层 `STAIR`｜源 `E000003 ` → 重绘 `R000003`
9. `draw_line`｜图层 `STAIR`｜源 `E000004 ` → 重绘 `R000004`
10. `draw_line`｜图层 `STAIR`｜源 `E000005 ` → 重绘 `R000005`
11. `draw_line`｜图层 `PUB_DIM`｜源 `E000006 ` → 重绘 `R000006`
12. `draw_line`｜图层 `PUB_DIM`｜源 `E000007 ` → 重绘 `R000007`
13. `draw_line`｜图层 `PUB_DIM`｜源 `E000008 ` → 重绘 `R000008`
14. `draw_line`｜图层 `PUB_DIM`｜源 `E000009 ` → 重绘 `R000009`
15. `draw_line`｜图层 `PUB_DIM`｜源 `E000010 ` → 重绘 `R000010`
16. `draw_line`｜图层 `PUB_DIM`｜源 `E000011 ` → 重绘 `R000011`
17. `draw_line`｜图层 `PUB_DIM`｜源 `E000012 ` → 重绘 `R000012`
18. `draw_line`｜图层 `PUB_DIM`｜源 `E000013 ` → 重绘 `R000013`
19. `draw_line`｜图层 `PUB_DIM`｜源 `E000014 ` → 重绘 `R000014`
20. `draw_line`｜图层 `PUB_DIM`｜源 `E000015 ` → 重绘 `R000015`
21. `draw_line`｜图层 `PUB_DIM`｜源 `E000016 ` → 重绘 `R000016`
