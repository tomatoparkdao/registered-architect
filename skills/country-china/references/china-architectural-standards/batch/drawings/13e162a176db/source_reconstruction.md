# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`FH01F064.DWG`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[-2258.11, -1.03], [-658.11, 2098.97]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `7`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `BH`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `3`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `2`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `1`｜源 `- ` → 重绘 `-`
7. `create_layer`｜图层 `4`｜源 `- ` → 重绘 `-`
8. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
9. `draw_polyline`｜图层 `3`｜源 `E000001 ` → 重绘 `R000001`
10. `draw_line`｜图层 `7`｜源 `E000002 ` → 重绘 `R000002`
11. `draw_polyline`｜图层 `4`｜源 `E000003 ` → 重绘 `R000003`
12. `draw_polyline`｜图层 `4`｜源 `E000004 ` → 重绘 `R000004`
13. `draw_polyline`｜图层 `3`｜源 `E000005 ` → 重绘 `R000005`
14. `hatch`｜图层 `BH`｜源 `E000006 ` → 重绘 `R000006`
15. `draw_polyline`｜图层 `3`｜源 `E000007 ` → 重绘 `R000007`
16. `draw_polyline`｜图层 `4`｜源 `E000008 ` → 重绘 `R000008`
17. `draw_polyline`｜图层 `4`｜源 `E000009 ` → 重绘 `R000009`
18. `draw_polyline`｜图层 `3`｜源 `E000010 ` → 重绘 `R000010`
19. `draw_polyline`｜图层 `3`｜源 `E000011 ` → 重绘 `R000011`
20. `draw_polyline`｜图层 `3`｜源 `E000012 ` → 重绘 `R000012`
21. `draw_polyline`｜图层 `3`｜源 `E000013 ` → 重绘 `R000013`
22. `hatch`｜图层 `BH`｜源 `E000014 ` → 重绘 `R000014`
23. `draw_polyline`｜图层 `7`｜源 `E000015 ` → 重绘 `R000015`
24. `draw_polyline`｜图层 `7`｜源 `E000016 ` → 重绘 `R000016`
25. `draw_line`｜图层 `2`｜源 `E000017 ` → 重绘 `R000017`
26. `draw_polyline`｜图层 `3`｜源 `E000018 ` → 重绘 `R000018`
27. `draw_polyline`｜图层 `3`｜源 `E000019 ` → 重绘 `R000019`
28. `hatch`｜图层 `BH`｜源 `E000020 ` → 重绘 `R000020`
29. `draw_circle`｜图层 `1`｜源 `E000021 ` → 重绘 `R000021`
30. `draw_circle`｜图层 `7`｜源 `E000022 ` → 重绘 `R000022`
31. `draw_circle`｜图层 `1`｜源 `E000023 ` → 重绘 `R000023`
32. `draw_circle`｜图层 `7`｜源 `E000024 ` → 重绘 `R000024`
33. `draw_circle`｜图层 `7`｜源 `E000025 ` → 重绘 `R000025`
34. `draw_polyline`｜图层 `7`｜源 `E000026 ` → 重绘 `R000026`
35. `draw_polyline`｜图层 `7`｜源 `E000027 ` → 重绘 `R000027`
36. `draw_polyline`｜图层 `3`｜源 `E000028 ` → 重绘 `R000028`
37. `draw_polyline`｜图层 `3`｜源 `E000029 ` → 重绘 `R000029`
38. `hatch`｜图层 `BH`｜源 `E000030 ` → 重绘 `R000030`
39. `draw_circle`｜图层 `7`｜源 `E000031 ` → 重绘 `R000031`
40. `draw_line`｜图层 `3`｜源 `E000032 ` → 重绘 `R000032`
41. `draw_line`｜图层 `3`｜源 `E000033 ` → 重绘 `R000033`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
