# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`阀门.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[0.0, 0.0], [165.42, 571.01]]`。
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
27. `insert_block`｜图层 `0`｜源 `E000001 ` → 重绘 `R000001`
28. `insert_block`｜图层 `0`｜源 `E000002 ` → 重绘 `R000002`
29. `insert_block`｜图层 `0`｜源 `E000003 ` → 重绘 `R000003`
30. `insert_block`｜图层 `0`｜源 `E000004 ` → 重绘 `R000004`
31. `insert_block`｜图层 `0`｜源 `E000005 ` → 重绘 `R000005`
32. `insert_block`｜图层 `0`｜源 `E000006 ` → 重绘 `R000006`
33. `insert_block`｜图层 `0`｜源 `E000007 ` → 重绘 `R000007`
34. `insert_block`｜图层 `0`｜源 `E000008 ` → 重绘 `R000008`
35. `insert_block`｜图层 `0`｜源 `E000009 ` → 重绘 `R000009`
36. `insert_block`｜图层 `0`｜源 `E000010 ` → 重绘 `R000010`
37. `insert_block`｜图层 `0`｜源 `E000011 ` → 重绘 `R000011`
38. `insert_block`｜图层 `0`｜源 `E000012 ` → 重绘 `R000012`
39. `insert_block`｜图层 `0`｜源 `E000013 ` → 重绘 `R000013`
40. `insert_block`｜图层 `0`｜源 `E000014 ` → 重绘 `R000014`
41. `insert_block`｜图层 `0`｜源 `E000015 ` → 重绘 `R000015`
42. `insert_block`｜图层 `0`｜源 `E000016 ` → 重绘 `R000016`
43. `insert_block`｜图层 `0`｜源 `E000017 ` → 重绘 `R000017`
44. `insert_block`｜图层 `0`｜源 `E000018 ` → 重绘 `R000018`
45. `insert_block`｜图层 `0`｜源 `E000019 ` → 重绘 `R000019`
46. `insert_block`｜图层 `0`｜源 `E000020 ` → 重绘 `R000020`
47. `insert_block`｜图层 `0`｜源 `E000021 ` → 重绘 `R000021`
48. `insert_block`｜图层 `0`｜源 `E000022 ` → 重绘 `R000022`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
