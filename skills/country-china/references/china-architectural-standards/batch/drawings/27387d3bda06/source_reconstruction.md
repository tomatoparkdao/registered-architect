# 源图重绘配方

- 源 DWG：`阳台砼栏板大样02.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[6596.9, 19296.92], [7964.89, 21277.63]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `DEFPOINTS`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `WALL`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `LINE`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `PUB_DIM`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `PUB_TEXT`｜源 `- ` → 重绘 `-`
7. `create_layer`｜图层 `PUB_HATCH`｜源 `- ` → 重绘 `-`
8. `create_layer`｜图层 `PUB_WALL`｜源 `- ` → 重绘 `-`
9. `create_layer`｜图层 `OTHER`｜源 `- ` → 重绘 `-`
10. `create_layer`｜图层 `S_FLOOR`｜源 `- ` → 重绘 `-`
11. `draw_line`｜图层 `LINE`｜源 `E000001 ` → 重绘 `R000001`
12. `draw_line`｜图层 `LINE`｜源 `E000003 ` → 重绘 `R000003`
13. `draw_line`｜图层 `WALL`｜源 `E000004 ` → 重绘 `R000004`
14. `draw_line`｜图层 `LINE`｜源 `E000005 ` → 重绘 `R000005`
15. `draw_line`｜图层 `PUB_DIM`｜源 `E000006 ` → 重绘 `R000006`
16. `draw_line`｜图层 `WALL`｜源 `E000007 ` → 重绘 `R000007`
17. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000009 ` → 重绘 `R000009`
18. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000010 ` → 重绘 `R000010`
19. `draw_polyline`｜图层 `PUB_WALL`｜源 `E000011 ` → 重绘 `R000011`
20. `draw_line`｜图层 `PUB_DIM`｜源 `E000013 ` → 重绘 `R000013`
21. `draw_line`｜图层 `PUB_DIM`｜源 `E000014 ` → 重绘 `R000014`
22. `draw_line`｜图层 `PUB_DIM`｜源 `E000018 ` → 重绘 `R000018`
23. `draw_line`｜图层 `LINE`｜源 `E000023 ` → 重绘 `R000023`
24. `draw_line`｜图层 `LINE`｜源 `E000024 ` → 重绘 `R000024`
25. `draw_line`｜图层 `LINE`｜源 `E000025 ` → 重绘 `R000025`
26. `draw_line`｜图层 `WALL`｜源 `E000026 ` → 重绘 `R000026`
27. `draw_line`｜图层 `LINE`｜源 `E000027 ` → 重绘 `R000027`
28. `draw_line`｜图层 `LINE`｜源 `E000028 ` → 重绘 `R000028`
29. `draw_line`｜图层 `WALL`｜源 `E000029 ` → 重绘 `R000029`
30. `draw_line`｜图层 `LINE`｜源 `E000030 ` → 重绘 `R000030`
31. `draw_line`｜图层 `WALL`｜源 `E000031 ` → 重绘 `R000031`
32. `draw_line`｜图层 `LINE`｜源 `E000032 ` → 重绘 `R000032`
33. `draw_line`｜图层 `WALL`｜源 `E000033 ` → 重绘 `R000033`
34. `draw_line`｜图层 `PUB_DIM`｜源 `E000037 ` → 重绘 `R000037`
35. `draw_line`｜图层 `LINE`｜源 `E000038 ` → 重绘 `R000038`
36. `draw_line`｜图层 `LINE`｜源 `E000039 ` → 重绘 `R000039`
37. `draw_line`｜图层 `LINE`｜源 `E000040 ` → 重绘 `R000040`
38. `draw_line`｜图层 `WALL`｜源 `E000041 ` → 重绘 `R000041`
39. `draw_line`｜图层 `WALL`｜源 `E000042 ` → 重绘 `R000042`
40. `draw_line`｜图层 `WALL`｜源 `E000043 ` → 重绘 `R000043`
41. `draw_line`｜图层 `LINE`｜源 `E000044 ` → 重绘 `R000044`
42. `draw_line`｜图层 `LINE`｜源 `E000045 ` → 重绘 `R000045`
43. `draw_line`｜图层 `LINE`｜源 `E000046 ` → 重绘 `R000046`
44. `draw_line`｜图层 `LINE`｜源 `E000047 ` → 重绘 `R000047`
45. `insert_block`｜图层 `LINE`｜源 `E000048 ` → 重绘 `R000048`
46. `insert_block`｜图层 `LINE`｜源 `E000049 ` → 重绘 `R000049`
47. `draw_line`｜图层 `OTHER`｜源 `E000050 ` → 重绘 `R000050`
48. `draw_line`｜图层 `OTHER`｜源 `E000051 ` → 重绘 `R000051`
49. `draw_line`｜图层 `OTHER`｜源 `E000052 ` → 重绘 `R000052`
50. `draw_line`｜图层 `OTHER`｜源 `E000053 ` → 重绘 `R000053`
51. `draw_line`｜图层 `OTHER`｜源 `E000054 ` → 重绘 `R000054`
52. `draw_line`｜图层 `LINE`｜源 `E000055 ` → 重绘 `R000055`
53. `draw_line`｜图层 `LINE`｜源 `E000056 ` → 重绘 `R000056`
54. `draw_polyline`｜图层 `PUB_DIM`｜源 `E000057 ` → 重绘 `R000057`
55. `insert_block`｜图层 `PUB_DIM`｜源 `E000058 ` → 重绘 `R000058`
56. `draw_line`｜图层 `LINE`｜源 `E000061 ` → 重绘 `R000061`
57. `insert_block`｜图层 `LINE`｜源 `E000062 ` → 重绘 `R000062`
58. `insert_block`｜图层 `LINE`｜源 `E000063 ` → 重绘 `R000063`
59. `insert_block`｜图层 `LINE`｜源 `E000064 ` → 重绘 `R000064`
60. `insert_block`｜图层 `LINE`｜源 `E000065 ` → 重绘 `R000065`
61. `draw_line`｜图层 `LINE`｜源 `E000066 ` → 重绘 `R000066`
62. `add_text`｜图层 `PUB_TEXT`｜源 `E000002 ` → 重绘 `R000002`
63. `add_text`｜图层 `PUB_TEXT`｜源 `E000008 ` → 重绘 `R000008`
64. `add_text`｜图层 `PUB_TEXT`｜源 `E000012 ` → 重绘 `R000012`
65. `add_text`｜图层 `PUB_TEXT`｜源 `E000015 ` → 重绘 `R000015`
66. `add_text`｜图层 `PUB_TEXT`｜源 `E000016 ` → 重绘 `R000016`
67. `add_text`｜图层 `PUB_DIM`｜源 `E000017 ` → 重绘 `R000017`
68. `add_text`｜图层 `PUB_TEXT`｜源 `E000019 ` → 重绘 `R000019`
69. `add_text`｜图层 `PUB_TEXT`｜源 `E000020 ` → 重绘 `R000020`
70. `add_text`｜图层 `PUB_TEXT`｜源 `E000034 ` → 重绘 `R000034`
71. `add_text`｜图层 `PUB_TEXT`｜源 `E000036 ` → 重绘 `R000036`
72. `add_text`｜图层 `PUB_TEXT`｜源 `E000059 ` → 重绘 `R000059`
73. `add_dimension`｜图层 `LINE`｜源 `E000021 ` → 重绘 `R000021`
74. `add_dimension`｜图层 `LINE`｜源 `E000022 ` → 重绘 `R000022`
75. `add_dimension`｜图层 `LINE`｜源 `E000035 ` → 重绘 `R000035`
76. `add_dimension`｜图层 `LINE`｜源 `E000060 ` → 重绘 `R000060`
