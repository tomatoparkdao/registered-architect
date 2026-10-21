# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`FH01A062.DWG`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[-605.35, 0.0], [-139.55, 823.07]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `3`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `4`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
5. `draw_polyline`｜图层 `3`｜源 `E000001 ` → 重绘 `R000001`
6. `draw_polyline`｜图层 `3`｜源 `E000002 ` → 重绘 `R000002`
7. `draw_polyline`｜图层 `3`｜源 `E000003 ` → 重绘 `R000003`
8. `draw_polyline`｜图层 `3`｜源 `E000004 ` → 重绘 `R000004`
9. `draw_polyline`｜图层 `3`｜源 `E000005 ` → 重绘 `R000005`
10. `draw_polyline`｜图层 `3`｜源 `E000006 ` → 重绘 `R000006`
11. `draw_polyline`｜图层 `3`｜源 `E000007 ` → 重绘 `R000007`
12. `draw_polyline`｜图层 `3`｜源 `E000008 ` → 重绘 `R000008`
13. `draw_polyline`｜图层 `4`｜源 `E000009 ` → 重绘 `R000009`
14. `draw_polyline`｜图层 `3`｜源 `E000010 ` → 重绘 `R000010`
15. `draw_polyline`｜图层 `3`｜源 `E000012 ` → 重绘 `R000012`
16. `draw_polyline`｜图层 `3`｜源 `E000013 ` → 重绘 `R000013`
17. `draw_polyline`｜图层 `3`｜源 `E000014 ` → 重绘 `R000014`
18. `draw_polyline`｜图层 `3`｜源 `E000015 ` → 重绘 `R000015`
19. `draw_polyline`｜图层 `3`｜源 `E000016 ` → 重绘 `R000016`
20. `draw_polyline`｜图层 `3`｜源 `E000018 ` → 重绘 `R000018`
21. `draw_polyline`｜图层 `3`｜源 `E000019 ` → 重绘 `R000019`
22. `draw_polyline`｜图层 `3`｜源 `E000020 ` → 重绘 `R000020`
23. `draw_polyline`｜图层 `3`｜源 `E000021 ` → 重绘 `R000021`
24. `draw_polyline`｜图层 `3`｜源 `E000025 ` → 重绘 `R000025`
25. `draw_polyline`｜图层 `4`｜源 `E000027 ` → 重绘 `R000027`
26. `draw_polyline`｜图层 `3`｜源 `E000028 ` → 重绘 `R000028`
27. `draw_polyline`｜图层 `3`｜源 `E000029 ` → 重绘 `R000029`
28. `draw_polyline`｜图层 `3`｜源 `E000030 ` → 重绘 `R000030`
29. `draw_polyline`｜图层 `3`｜源 `E000031 ` → 重绘 `R000031`
30. `draw_polyline`｜图层 `3`｜源 `E000032 ` → 重绘 `R000032`
31. `draw_polyline`｜图层 `3`｜源 `E000033 ` → 重绘 `R000033`
32. `draw_polyline`｜图层 `3`｜源 `E000036 ` → 重绘 `R000036`
33. `draw_polyline`｜图层 `3`｜源 `E000039 ` → 重绘 `R000039`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
