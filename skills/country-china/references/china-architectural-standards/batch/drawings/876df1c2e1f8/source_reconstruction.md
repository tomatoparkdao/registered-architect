# 源图重绘配方

- 源 DWG：`D371-bz.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[-312.84, -96.63], [1390.7, 948.43]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `tl`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `fl`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `b`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `c`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `d`｜源 `- ` → 重绘 `-`
7. `create_layer`｜图层 `ha`｜源 `- ` → 重绘 `-`
8. `create_layer`｜图层 `t`｜源 `- ` → 重绘 `-`
9. `create_layer`｜图层 `title`｜源 `- ` → 重绘 `-`
10. `create_layer`｜图层 `ls`｜源 `- ` → 重绘 `-`
11. `create_layer`｜图层 `e`｜源 `- ` → 重绘 `-`
12. `create_layer`｜图层 `ASHADE`｜源 `- ` → 重绘 `-`
13. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
14. `draw_polyline`｜图层 `title`｜源 `E000001 ` → 重绘 `R000001`
15. `draw_polyline`｜图层 `title`｜源 `E000002 ` → 重绘 `R000002`
16. `draw_line`｜图层 `title`｜源 `E000003 ` → 重绘 `R000003`
17. `add_leader`｜图层 `title`｜源 `E000004 ` → 重绘 `R000004`
18. `add_leader`｜图层 `title`｜源 `E000006 ` → 重绘 `R000006`
19. `add_leader`｜图层 `title`｜源 `E000007 ` → 重绘 `R000007`
20. `insert_block`｜图层 `ASHADE`｜源 `E000008 ` → 重绘 `R000008`
21. `insert_block`｜图层 `ASHADE`｜源 `E000009 ` → 重绘 `R000009`
22. `insert_block`｜图层 `ASHADE`｜源 `E000010 ` → 重绘 `R000010`
23. `insert_block`｜图层 `ASHADE`｜源 `E000011 ` → 重绘 `R000011`
24. `insert_block`｜图层 `ASHADE`｜源 `E000012 ` → 重绘 `R000012`
25. `insert_block`｜图层 `ASHADE`｜源 `E000013 ` → 重绘 `R000013`
26. `insert_block`｜图层 `ASHADE`｜源 `E000014 ` → 重绘 `R000014`
27. `insert_block`｜图层 `ASHADE`｜源 `E000015 ` → 重绘 `R000015`
28. `insert_block`｜图层 `ASHADE`｜源 `E000016 ` → 重绘 `R000016`
29. `draw_line`｜图层 `c`｜源 `E000017 ` → 重绘 `R000017`
30. `draw_line`｜图层 `c`｜源 `E000018 ` → 重绘 `R000018`
31. `draw_line`｜图层 `c`｜源 `E000019 ` → 重绘 `R000019`
32. `add_mtext`｜图层 `tl`｜源 `E000005 ` → 重绘 `R000005`
