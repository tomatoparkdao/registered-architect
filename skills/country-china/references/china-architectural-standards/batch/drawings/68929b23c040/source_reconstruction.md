# 源图重绘配方

- 源 DWG：`内外罗纹接头.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[0.0, -12.86], [25.7, 12.86]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `000_THIN`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `001_THICK`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `002_THIN`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `003_THICK`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `004_THIN`｜源 `- ` → 重绘 `-`
7. `create_layer`｜图层 `005_THICK`｜源 `- ` → 重绘 `-`
8. `create_layer`｜图层 `006_DASH0`｜源 `- ` → 重绘 `-`
9. `create_layer`｜图层 `007_DASH1`｜源 `- ` → 重绘 `-`
10. `create_layer`｜图层 `008_CENTER0`｜源 `- ` → 重绘 `-`
11. `create_layer`｜图层 `009_CENTER1`｜源 `- ` → 重绘 `-`
12. `create_layer`｜图层 `010_DASH_DDOT0`｜源 `- ` → 重绘 `-`
13. `create_layer`｜图层 `011_DASH_DDOT1`｜源 `- ` → 重绘 `-`
14. `create_layer`｜图层 `012_ZZ_LINE`｜源 `- ` → 重绘 `-`
15. `create_layer`｜图层 `013_DOT_LINE`｜源 `- ` → 重绘 `-`
16. `create_layer`｜图层 `014_FILL`｜源 `- ` → 重绘 `-`
17. `create_layer`｜图层 `015_TEXT`｜源 `- ` → 重绘 `-`
18. `create_layer`｜图层 `016_HEAD_LINE0`｜源 `- ` → 重绘 `-`
19. `create_layer`｜图层 `017_HEAD_LINE1`｜源 `- ` → 重绘 `-`
20. `create_layer`｜图层 `018_HEAD_TEXT0`｜源 `- ` → 重绘 `-`
21. `create_layer`｜图层 `019_HEAD_TEXT1`｜源 `- ` → 重绘 `-`
22. `create_layer`｜图层 `020_DIM_LINE0`｜源 `- ` → 重绘 `-`
23. `create_layer`｜图层 `021_DIM_LINE1`｜源 `- ` → 重绘 `-`
24. `create_layer`｜图层 `022_DIM_LINE2`｜源 `- ` → 重绘 `-`
25. `create_layer`｜图层 `023_DIM_TEXT`｜源 `- ` → 重绘 `-`
26. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
27. `draw_polyline`｜图层 `003_THICK`｜源 `E000001 ` → 重绘 `R000001`
28. `draw_polyline`｜图层 `003_THICK`｜源 `E000002 ` → 重绘 `R000002`
29. `draw_polyline`｜图层 `003_THICK`｜源 `E000003 ` → 重绘 `R000003`
30. `draw_polyline`｜图层 `003_THICK`｜源 `E000004 ` → 重绘 `R000004`
31. `draw_polyline`｜图层 `003_THICK`｜源 `E000005 ` → 重绘 `R000005`
32. `draw_polyline`｜图层 `003_THICK`｜源 `E000006 ` → 重绘 `R000006`
