# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`不锈钢扶手.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[3746.67, 10365.66], [5614.06, 11781.17]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `WALL`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `PUB_HATCH`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `配筋`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `PUB_TEXT`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `引出线`｜源 `- ` → 重绘 `-`
7. `create_layer`｜图层 `PUB_DIM`｜源 `- ` → 重绘 `-`
8. `create_layer`｜图层 `DEFPOINTS`｜源 `- ` → 重绘 `-`
9. `create_layer`｜图层 `SEE`｜源 `- ` → 重绘 `-`
10. `draw_line`｜图层 `引出线`｜源 `E000001 ` → 重绘 `R000001`
11. `draw_line`｜图层 `引出线`｜源 `E000002 ` → 重绘 `R000002`
12. `draw_line`｜图层 `PUB_DIM`｜源 `E000005 ` → 重绘 `R000005`
13. `draw_line`｜图层 `PUB_DIM`｜源 `E000006 ` → 重绘 `R000006`
14. `draw_line`｜图层 `PUB_DIM`｜源 `E000007 ` → 重绘 `R000007`
15. `hatch`｜图层 `PUB_HATCH`｜源 `E000008 ` → 重绘 `R000008`
16. `draw_line`｜图层 `WALL`｜源 `E000009 ` → 重绘 `R000009`
17. `draw_line`｜图层 `WALL`｜源 `E000010 ` → 重绘 `R000010`
18. `draw_line`｜图层 `SEE`｜源 `E000011 ` → 重绘 `R000011`
19. `draw_line`｜图层 `SEE`｜源 `E000012 ` → 重绘 `R000012`
20. `draw_line`｜图层 `PUB_DIM`｜源 `E000013 ` → 重绘 `R000013`
21. `draw_line`｜图层 `引出线`｜源 `E000014 ` → 重绘 `R000014`
22. `draw_line`｜图层 `PUB_DIM`｜源 `E000019 ` → 重绘 `R000019`
23. `insert_block`｜图层 `PUB_DIM`｜源 `E000020 ` → 重绘 `R000020`
24. `draw_line`｜图层 `SEE`｜源 `E000023 ` → 重绘 `R000023`
25. `draw_line`｜图层 `SEE`｜源 `E000024 ` → 重绘 `R000024`
26. `draw_line`｜图层 `WALL`｜源 `E000025 ` → 重绘 `R000025`
27. `draw_line`｜图层 `SEE`｜源 `E000026 ` → 重绘 `R000026`
28. `draw_line`｜图层 `PUB_TEXT`｜源 `E000027 ` → 重绘 `R000027`
29. `draw_line`｜图层 `WALL`｜源 `E000028 ` → 重绘 `R000028`
30. `draw_line`｜图层 `PUB_TEXT`｜源 `E000029 ` → 重绘 `R000029`
31. `hatch`｜图层 `PUB_HATCH`｜源 `E000030 ` → 重绘 `R000030`
32. `draw_line`｜图层 `WALL`｜源 `E000031 ` → 重绘 `R000031`
33. `draw_polyline`｜图层 `配筋`｜源 `E000032 ` → 重绘 `R000032`
34. `draw_line`｜图层 `WALL`｜源 `E000033 ` → 重绘 `R000033`
35. `draw_line`｜图层 `SEE`｜源 `E000034 ` → 重绘 `R000034`
36. `draw_polyline`｜图层 `配筋`｜源 `E000035 ` → 重绘 `R000035`
37. `draw_polyline`｜图层 `配筋`｜源 `E000036 ` → 重绘 `R000036`
38. `draw_line`｜图层 `SEE`｜源 `E000037 ` → 重绘 `R000037`
39. `draw_line`｜图层 `SEE`｜源 `E000038 ` → 重绘 `R000038`
40. `draw_polyline`｜图层 `配筋`｜源 `E000039 ` → 重绘 `R000039`
41. `draw_polyline`｜图层 `配筋`｜源 `E000040 ` → 重绘 `R000040`
42. `draw_line`｜图层 `SEE`｜源 `E000041 ` → 重绘 `R000041`
43. `draw_line`｜图层 `SEE`｜源 `E000042 ` → 重绘 `R000042`
44. `draw_line`｜图层 `SEE`｜源 `E000043 ` → 重绘 `R000043`
45. `draw_line`｜图层 `SEE`｜源 `E000044 ` → 重绘 `R000044`
46. `draw_line`｜图层 `WALL`｜源 `E000045 ` → 重绘 `R000045`
47. `draw_line`｜图层 `WALL`｜源 `E000046 ` → 重绘 `R000046`
48. `draw_line`｜图层 `WALL`｜源 `E000047 ` → 重绘 `R000047`
49. `draw_circle`｜图层 `SEE`｜源 `E000049 ` → 重绘 `R000049`
50. `draw_circle`｜图层 `SEE`｜源 `E000050 ` → 重绘 `R000050`
51. `draw_line`｜图层 `PUB_DIM`｜源 `E000053 ` → 重绘 `R000053`
52. `draw_line`｜图层 `PUB_DIM`｜源 `E000054 ` → 重绘 `R000054`
53. `draw_line`｜图层 `引出线`｜源 `E000057 ` → 重绘 `R000057`
54. `draw_line`｜图层 `引出线`｜源 `E000058 ` → 重绘 `R000058`
55. `draw_line`｜图层 `引出线`｜源 `E000061 ` → 重绘 `R000061`
56. `add_text`｜图层 `PUB_TEXT`｜源 `E000003 ` → 重绘 `R000003`
57. `add_text`｜图层 `PUB_TEXT`｜源 `E000015 ` → 重绘 `R000015`
58. `add_text`｜图层 `PUB_TEXT`｜源 `E000016 ` → 重绘 `R000016`
59. `add_text`｜图层 `PUB_TEXT`｜源 `E000017 ` → 重绘 `R000017`
60. `add_text`｜图层 `PUB_TEXT`｜源 `E000018 ` → 重绘 `R000018`
61. `add_text`｜图层 `PUB_TEXT`｜源 `E000021 ` → 重绘 `R000021`
62. `add_text`｜图层 `PUB_DIM`｜源 `E000051 ` → 重绘 `R000051`
63. `add_text`｜图层 `PUB_DIM`｜源 `E000052 ` → 重绘 `R000052`
64. `add_text`｜图层 `PUB_TEXT`｜源 `E000055 ` → 重绘 `R000055`
65. `add_text`｜图层 `PUB_TEXT`｜源 `E000056 ` → 重绘 `R000056`
66. `add_text`｜图层 `PUB_TEXT`｜源 `E000059 ` → 重绘 `R000059`
67. `add_text`｜图层 `PUB_TEXT`｜源 `E000060 ` → 重绘 `R000060`
68. `add_text`｜图层 `PUB_TEXT`｜源 `E000062 ` → 重绘 `R000062`
69. `add_text`｜图层 `PUB_TEXT`｜源 `E000063 ` → 重绘 `R000063`
70. `add_text`｜图层 `PUB_TEXT`｜源 `E000064 ` → 重绘 `R000064`
71. `add_text`｜图层 `PUB_TEXT`｜源 `E000065 ` → 重绘 `R000065`
72. `add_text`｜图层 `PUB_TEXT`｜源 `E000066 ` → 重绘 `R000066`
73. `add_dimension`｜图层 `PUB_DIM`｜源 `E000004 ` → 重绘 `R000004`
74. `add_dimension`｜图层 `PUB_DIM`｜源 `E000022 ` → 重绘 `R000022`
75. `add_dimension`｜图层 `PUB_DIM`｜源 `E000048 ` → 重绘 `R000048`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
