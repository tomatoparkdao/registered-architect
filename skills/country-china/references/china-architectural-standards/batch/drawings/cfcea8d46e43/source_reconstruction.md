# 源图重绘配方

- 源 DWG：`DY-女儿墙压顶及泛水.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[7699.42, 11071.94], [8592.61, 12200.39]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `PUB_DIM`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `DEFPOINTS`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `PUB_TEXT`｜源 `- ` → 重绘 `-`
5. `draw_polyline`｜图层 `0`｜源 `E000001 ` → 重绘 `R000001`
6. `draw_polyline`｜图层 `0`｜源 `E000002 ` → 重绘 `R000002`
7. `draw_polyline`｜图层 `0`｜源 `E000003 ` → 重绘 `R000003`
8. `draw_polyline`｜图层 `0`｜源 `E000004 ` → 重绘 `R000004`
9. `draw_polyline`｜图层 `0`｜源 `E000005 ` → 重绘 `R000005`
10. `draw_polyline`｜图层 `0`｜源 `E000006 ` → 重绘 `R000006`
11. `draw_polyline`｜图层 `0`｜源 `E000007 ` → 重绘 `R000007`
12. `hatch`｜图层 `0`｜源 `E000010 ` → 重绘 `R000010`
13. `hatch`｜图层 `0`｜源 `E000011 ` → 重绘 `R000011`
14. `draw_circle`｜图层 `0`｜源 `E000012 ` → 重绘 `R000012`
15. `hatch`｜图层 `0`｜源 `E000013 ` → 重绘 `R000013`
16. `hatch`｜图层 `0`｜源 `E000014 ` → 重绘 `R000014`
17. `draw_circle`｜图层 `0`｜源 `E000015 ` → 重绘 `R000015`
18. `hatch`｜图层 `0`｜源 `E000016 ` → 重绘 `R000016`
19. `draw_circle`｜图层 `0`｜源 `E000017 ` → 重绘 `R000017`
20. `hatch`｜图层 `0`｜源 `E000018 ` → 重绘 `R000018`
21. `draw_line`｜图层 `PUB_TEXT`｜源 `E000019 ` → 重绘 `R000019`
22. `draw_line`｜图层 `PUB_TEXT`｜源 `E000021 ` → 重绘 `R000021`
23. `draw_line`｜图层 `PUB_TEXT`｜源 `E000022 ` → 重绘 `R000022`
24. `draw_line`｜图层 `PUB_TEXT`｜源 `E000023 ` → 重绘 `R000023`
25. `draw_line`｜图层 `PUB_TEXT`｜源 `E000024 ` → 重绘 `R000024`
26. `draw_line`｜图层 `PUB_TEXT`｜源 `E000025 ` → 重绘 `R000025`
27. `draw_line`｜图层 `PUB_TEXT`｜源 `E000026 ` → 重绘 `R000026`
28. `draw_line`｜图层 `PUB_TEXT`｜源 `E000034 ` → 重绘 `R000034`
29. `draw_line`｜图层 `PUB_TEXT`｜源 `E000035 ` → 重绘 `R000035`
30. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000038 ` → 重绘 `R000038`
31. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000039 ` → 重绘 `R000039`
32. `add_text`｜图层 `PUB_TEXT`｜源 `E000020 ` → 重绘 `R000020`
33. `add_text`｜图层 `PUB_TEXT`｜源 `E000027 ` → 重绘 `R000027`
34. `add_text`｜图层 `PUB_TEXT`｜源 `E000028 ` → 重绘 `R000028`
35. `add_text`｜图层 `PUB_TEXT`｜源 `E000029 ` → 重绘 `R000029`
36. `add_text`｜图层 `PUB_TEXT`｜源 `E000030 ` → 重绘 `R000030`
37. `add_text`｜图层 `PUB_TEXT`｜源 `E000036 ` → 重绘 `R000036`
38. `add_text`｜图层 `PUB_TEXT`｜源 `E000037 ` → 重绘 `R000037`
39. `add_dimension`｜图层 `PUB_DIM`｜源 `E000008 ` → 重绘 `R000008`
40. `add_dimension`｜图层 `PUB_DIM`｜源 `E000009 ` → 重绘 `R000009`
41. `add_dimension`｜图层 `PUB_DIM`｜源 `E000031 ` → 重绘 `R000031`
42. `add_dimension`｜图层 `PUB_DIM`｜源 `E000032 ` → 重绘 `R000032`
43. `add_dimension`｜图层 `PUB_DIM`｜源 `E000033 ` → 重绘 `R000033`
