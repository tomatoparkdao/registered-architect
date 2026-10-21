# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`_Q28NDH.DWG`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[9293.89, 11909.04], [12397.69, 13816.9]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `DEFPOINTS`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `PUB_DIM`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `PUB_TEXT`｜源 `- ` → 重绘 `-`
5. `draw_polyline`｜图层 `0`｜源 `E000002 ` → 重绘 `R000002`
6. `insert_block`｜图层 `0`｜源 `E000003 ` → 重绘 `R000003`
7. `insert_block`｜图层 `0`｜源 `E000004 ` → 重绘 `R000004`
8. `insert_block`｜图层 `0`｜源 `E000005 ` → 重绘 `R000005`
9. `insert_block`｜图层 `0`｜源 `E000006 ` → 重绘 `R000006`
10. `draw_polyline`｜图层 `0`｜源 `E000007 ` → 重绘 `R000007`
11. `draw_polyline`｜图层 `0`｜源 `E000008 ` → 重绘 `R000008`
12. `draw_polyline`｜图层 `PUB_DIM`｜源 `E000009 ` → 重绘 `R000009`
13. `draw_polyline`｜图层 `0`｜源 `E000013 ` → 重绘 `R000013`
14. `insert_block`｜图层 `0`｜源 `E000014 ` → 重绘 `R000014`
15. `insert_block`｜图层 `0`｜源 `E000015 ` → 重绘 `R000015`
16. `draw_circle`｜图层 `PUB_DIM`｜源 `E000016 ` → 重绘 `R000016`
17. `draw_polyline`｜图层 `PUB_DIM`｜源 `E000017 ` → 重绘 `R000017`
18. `insert_block`｜图层 `0`｜源 `E000018 ` → 重绘 `R000018`
19. `draw_polyline`｜图层 `0`｜源 `E000019 ` → 重绘 `R000019`
20. `draw_polyline`｜图层 `0`｜源 `E000021 ` → 重绘 `R000021`
21. `insert_block`｜图层 `0`｜源 `E000022 ` → 重绘 `R000022`
22. `insert_block`｜图层 `0`｜源 `E000023 ` → 重绘 `R000023`
23. `draw_line`｜图层 `PUB_DIM`｜源 `E000027 ` → 重绘 `R000027`
24. `draw_line`｜图层 `PUB_DIM`｜源 `E000028 ` → 重绘 `R000028`
25. `draw_line`｜图层 `PUB_DIM`｜源 `E000029 ` → 重绘 `R000029`
26. `insert_block`｜图层 `0`｜源 `E000036 ` → 重绘 `R000036`
27. `draw_polyline`｜图层 `0`｜源 `E000037 ` → 重绘 `R000037`
28. `draw_line`｜图层 `0`｜源 `E000038 ` → 重绘 `R000038`
29. `draw_polyline`｜图层 `0`｜源 `E000039 ` → 重绘 `R000039`
30. `insert_block`｜图层 `0`｜源 `E000040 ` → 重绘 `R000040`
31. `draw_line`｜图层 `0`｜源 `E000042 ` → 重绘 `R000042`
32. `draw_polyline`｜图层 `0`｜源 `E000043 ` → 重绘 `R000043`
33. `add_text`｜图层 `PUB_TEXT`｜源 `E000001 ` → 重绘 `R000001`
34. `add_text`｜图层 `PUB_TEXT`｜源 `E000024 ` → 重绘 `R000024`
35. `add_text`｜图层 `PUB_TEXT`｜源 `E000025 ` → 重绘 `R000025`
36. `add_text`｜图层 `PUB_TEXT`｜源 `E000026 ` → 重绘 `R000026`
37. `add_text`｜图层 `PUB_TEXT`｜源 `E000030 ` → 重绘 `R000030`
38. `add_text`｜图层 `PUB_TEXT`｜源 `E000031 ` → 重绘 `R000031`
39. `add_text`｜图层 `PUB_TEXT`｜源 `E000032 ` → 重绘 `R000032`
40. `add_text`｜图层 `PUB_TEXT`｜源 `E000033 ` → 重绘 `R000033`
41. `add_text`｜图层 `PUB_TEXT`｜源 `E000034 ` → 重绘 `R000034`
42. `add_text`｜图层 `PUB_TEXT`｜源 `E000035 ` → 重绘 `R000035`
43. `add_text`｜图层 `PUB_TEXT`｜源 `E000044 ` → 重绘 `R000044`
44. `add_text`｜图层 `PUB_TEXT`｜源 `E000045 ` → 重绘 `R000045`
45. `add_dimension`｜图层 `PUB_DIM`｜源 `E000010 ` → 重绘 `R000010`
46. `add_dimension`｜图层 `PUB_DIM`｜源 `E000011 ` → 重绘 `R000011`
47. `add_dimension`｜图层 `PUB_DIM`｜源 `E000012 ` → 重绘 `R000012`
48. `add_dimension`｜图层 `PUB_DIM`｜源 `E000020 ` → 重绘 `R000020`
49. `add_dimension`｜图层 `PUB_DIM`｜源 `E000041 ` → 重绘 `R000041`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
