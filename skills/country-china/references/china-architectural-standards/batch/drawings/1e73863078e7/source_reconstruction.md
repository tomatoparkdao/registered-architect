# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`螺栓连接1.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[-176064.34, -367097.5], [-173532.64, -365697.53]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `AXIS`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `TEXT`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `DIM`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `K`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
7. `draw_line`｜图层 `AXIS`｜源 `E000001 ` → 重绘 `R000001`
8. `draw_line`｜图层 `AXIS`｜源 `E000002 ` → 重绘 `R000002`
9. `draw_line`｜图层 `K`｜源 `E000003 ` → 重绘 `R000003`
10. `draw_line`｜图层 `K`｜源 `E000004 ` → 重绘 `R000004`
11. `draw_line`｜图层 `K`｜源 `E000005 ` → 重绘 `R000005`
12. `draw_line`｜图层 `K`｜源 `E000006 ` → 重绘 `R000006`
13. `draw_line`｜图层 `AXIS`｜源 `E000007 ` → 重绘 `R000007`
14. `draw_line`｜图层 `K`｜源 `E000008 ` → 重绘 `R000008`
15. `draw_line`｜图层 `K`｜源 `E000009 ` → 重绘 `R000009`
16. `draw_line`｜图层 `K`｜源 `E000010 ` → 重绘 `R000010`
17. `draw_line`｜图层 `K`｜源 `E000011 ` → 重绘 `R000011`
18. `draw_line`｜图层 `TEXT`｜源 `E000012 ` → 重绘 `R000012`
19. `draw_line`｜图层 `TEXT`｜源 `E000013 ` → 重绘 `R000013`
20. `draw_line`｜图层 `TEXT`｜源 `E000014 ` → 重绘 `R000014`
21. `draw_line`｜图层 `TEXT`｜源 `E000015 ` → 重绘 `R000015`
22. `draw_line`｜图层 `TEXT`｜源 `E000016 ` → 重绘 `R000016`
23. `draw_circle`｜图层 `DIM`｜源 `E000017 ` → 重绘 `R000017`
24. `draw_line`｜图层 `DIM`｜源 `E000018 ` → 重绘 `R000018`
25. `draw_line`｜图层 `TEXT`｜源 `E000020 ` → 重绘 `R000020`
26. `draw_line`｜图层 `AXIS`｜源 `E000024 ` → 重绘 `R000024`
27. `draw_line`｜图层 `AXIS`｜源 `E000025 ` → 重绘 `R000025`
28. `draw_line`｜图层 `K`｜源 `E000026 ` → 重绘 `R000026`
29. `draw_line`｜图层 `K`｜源 `E000027 ` → 重绘 `R000027`
30. `draw_line`｜图层 `K`｜源 `E000028 ` → 重绘 `R000028`
31. `draw_line`｜图层 `K`｜源 `E000029 ` → 重绘 `R000029`
32. `draw_line`｜图层 `TEXT`｜源 `E000030 ` → 重绘 `R000030`
33. `draw_line`｜图层 `TEXT`｜源 `E000031 ` → 重绘 `R000031`
34. `draw_line`｜图层 `TEXT`｜源 `E000032 ` → 重绘 `R000032`
35. `draw_line`｜图层 `TEXT`｜源 `E000033 ` → 重绘 `R000033`
36. `draw_line`｜图层 `TEXT`｜源 `E000034 ` → 重绘 `R000034`
37. `draw_line`｜图层 `K`｜源 `E000035 ` → 重绘 `R000035`
38. `draw_line`｜图层 `K`｜源 `E000036 ` → 重绘 `R000036`
39. `draw_line`｜图层 `AXIS`｜源 `E000037 ` → 重绘 `R000037`
40. `draw_line`｜图层 `TEXT`｜源 `E000038 ` → 重绘 `R000038`
41. `add_text`｜图层 `DIM`｜源 `E000019 ` → 重绘 `R000019`
42. `add_text`｜图层 `DIM`｜源 `E000021 ` → 重绘 `R000021`
43. `add_text`｜图层 `DIM`｜源 `E000022 ` → 重绘 `R000022`
44. `add_text`｜图层 `DIM`｜源 `E000023 ` → 重绘 `R000023`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
