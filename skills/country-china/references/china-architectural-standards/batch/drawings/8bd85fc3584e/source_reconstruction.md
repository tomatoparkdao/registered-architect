# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`125jw07.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[0.0, 0.0], [184.5, 290.67]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `TL`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `FL`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `C`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `D`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `HA`｜源 `- ` → 重绘 `-`
7. `create_layer`｜图层 `T`｜源 `- ` → 重绘 `-`
8. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
9. `draw_line`｜图层 `D`｜源 `E000002 ` → 重绘 `R000002`
10. `draw_line`｜图层 `D`｜源 `E000003 ` → 重绘 `R000003`
11. `draw_polyline`｜图层 `TL`｜源 `E000007 ` → 重绘 `R000007`
12. `draw_polyline`｜图层 `TL`｜源 `E000008 ` → 重绘 `R000008`
13. `insert_block`｜图层 `HA`｜源 `E000009 ` → 重绘 `R000009`
14. `draw_line`｜图层 `D`｜源 `E000010 ` → 重绘 `R000010`
15. `draw_line`｜图层 `D`｜源 `E000011 ` → 重绘 `R000011`
16. `draw_line`｜图层 `D`｜源 `E000012 ` → 重绘 `R000012`
17. `draw_solid`｜图层 `D`｜源 `E000013 ` → 重绘 `R000013`
18. `draw_line`｜图层 `D`｜源 `E000014 ` → 重绘 `R000014`
19. `draw_solid`｜图层 `D`｜源 `E000015 ` → 重绘 `R000015`
20. `draw_polyline`｜图层 `TL`｜源 `E000016 ` → 重绘 `R000016`
21. `draw_polyline`｜图层 `C`｜源 `E000022 ` → 重绘 `R000022`
22. `draw_line`｜图层 `D`｜源 `E000024 ` → 重绘 `R000024`
23. `draw_solid`｜图层 `D`｜源 `E000025 ` → 重绘 `R000025`
24. `draw_solid`｜图层 `D`｜源 `E000026 ` → 重绘 `R000026`
25. `draw_line`｜图层 `D`｜源 `E000027 ` → 重绘 `R000027`
26. `draw_polyline`｜图层 `TL`｜源 `E000028 ` → 重绘 `R000028`
27. `draw_line`｜图层 `D`｜源 `E000033 ` → 重绘 `R000033`
28. `draw_line`｜图层 `D`｜源 `E000034 ` → 重绘 `R000034`
29. `draw_line`｜图层 `D`｜源 `E000035 ` → 重绘 `R000035`
30. `draw_solid`｜图层 `D`｜源 `E000036 ` → 重绘 `R000036`
31. `draw_solid`｜图层 `D`｜源 `E000037 ` → 重绘 `R000037`
32. `draw_line`｜图层 `D`｜源 `E000038 ` → 重绘 `R000038`
33. `insert_block`｜图层 `D`｜源 `E000039 ` → 重绘 `R000039`
34. `add_text`｜图层 `D`｜源 `E000001 ` → 重绘 `R000001`
35. `add_text`｜图层 `D`｜源 `E000004 ` → 重绘 `R000004`
36. `add_text`｜图层 `D`｜源 `E000005 ` → 重绘 `R000005`
37. `add_text`｜图层 `D`｜源 `E000006 ` → 重绘 `R000006`
38. `add_text`｜图层 `D`｜源 `E000017 ` → 重绘 `R000017`
39. `add_text`｜图层 `D`｜源 `E000018 ` → 重绘 `R000018`
40. `add_text`｜图层 `D`｜源 `E000019 ` → 重绘 `R000019`
41. `add_text`｜图层 `D`｜源 `E000020 ` → 重绘 `R000020`
42. `add_text`｜图层 `D`｜源 `E000021 ` → 重绘 `R000021`
43. `add_text`｜图层 `D`｜源 `E000023 ` → 重绘 `R000023`
44. `add_text`｜图层 `D`｜源 `E000029 ` → 重绘 `R000029`
45. `add_text`｜图层 `D`｜源 `E000030 ` → 重绘 `R000030`
46. `add_text`｜图层 `D`｜源 `E000031 ` → 重绘 `R000031`
47. `add_text`｜图层 `D`｜源 `E000032 ` → 重绘 `R000032`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
