# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`350zw01.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[0.0, 0.0], [814.88, 582.19]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `TL`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `FL`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `B`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `C`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `D`｜源 `- ` → 重绘 `-`
7. `create_layer`｜图层 `HA`｜源 `- ` → 重绘 `-`
8. `create_layer`｜图层 `T`｜源 `- ` → 重绘 `-`
9. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
10. `insert_block`｜图层 `D`｜源 `E000003 ` → 重绘 `R000003`
11. `draw_line`｜图层 `D`｜源 `E000018 ` → 重绘 `R000018`
12. `draw_line`｜图层 `D`｜源 `E000019 ` → 重绘 `R000019`
13. `draw_circle`｜图层 `D`｜源 `E000020 ` → 重绘 `R000020`
14. `draw_line`｜图层 `C`｜源 `E000021 ` → 重绘 `R000021`
15. `insert_block`｜图层 `D`｜源 `E000026 ` → 重绘 `R000026`
16. `add_text`｜图层 `D`｜源 `E000001 ` → 重绘 `R000001`
17. `add_text`｜图层 `D`｜源 `E000002 ` → 重绘 `R000002`
18. `add_text`｜图层 `D`｜源 `E000004 ` → 重绘 `R000004`
19. `add_text`｜图层 `D`｜源 `E000005 ` → 重绘 `R000005`
20. `add_text`｜图层 `D`｜源 `E000006 ` → 重绘 `R000006`
21. `add_text`｜图层 `D`｜源 `E000007 ` → 重绘 `R000007`
22. `add_text`｜图层 `D`｜源 `E000008 ` → 重绘 `R000008`
23. `add_text`｜图层 `D`｜源 `E000009 ` → 重绘 `R000009`
24. `add_text`｜图层 `D`｜源 `E000010 ` → 重绘 `R000010`
25. `add_text`｜图层 `D`｜源 `E000011 ` → 重绘 `R000011`
26. `add_text`｜图层 `D`｜源 `E000012 ` → 重绘 `R000012`
27. `add_text`｜图层 `D`｜源 `E000013 ` → 重绘 `R000013`
28. `add_text`｜图层 `D`｜源 `E000014 ` → 重绘 `R000014`
29. `add_text`｜图层 `D`｜源 `E000015 ` → 重绘 `R000015`
30. `add_text`｜图层 `D`｜源 `E000016 ` → 重绘 `R000016`
31. `add_text`｜图层 `D`｜源 `E000017 ` → 重绘 `R000017`
32. `add_text`｜图层 `D`｜源 `E000022 ` → 重绘 `R000022`
33. `add_text`｜图层 `D`｜源 `E000023 ` → 重绘 `R000023`
34. `add_text`｜图层 `D`｜源 `E000024 ` → 重绘 `R000024`
35. `add_text`｜图层 `D`｜源 `E000025 ` → 重绘 `R000025`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
