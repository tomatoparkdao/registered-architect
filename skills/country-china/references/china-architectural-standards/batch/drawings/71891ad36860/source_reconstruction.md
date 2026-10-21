# 源图重绘配方

- 源 DWG：`楼梯扶手1.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[-1378.89, 366.38], [-177.84, 1503.08]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `PUB_TEXT`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `S_SURFACE`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `PUB_WALL`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `DEFPOINTS`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `PUB_DIM`｜源 `- ` → 重绘 `-`
7. `create_layer`｜图层 `S_FLOOR`｜源 `- ` → 重绘 `-`
8. `create_layer`｜图层 `S_WALL`｜源 `- ` → 重绘 `-`
9. `draw_line`｜图层 `S_SURFACE`｜源 `E000001 ` → 重绘 `R000001`
10. `draw_line`｜图层 `S_WALL`｜源 `E000004 ` → 重绘 `R000004`
11. `draw_line`｜图层 `S_WALL`｜源 `E000005 ` → 重绘 `R000005`
12. `draw_polyline`｜图层 `PUB_WALL`｜源 `E000006 ` → 重绘 `R000006`
13. `draw_polyline`｜图层 `PUB_WALL`｜源 `E000007 ` → 重绘 `R000007`
14. `draw_line`｜图层 `S_SURFACE`｜源 `E000008 ` → 重绘 `R000008`
15. `draw_line`｜图层 `S_SURFACE`｜源 `E000009 ` → 重绘 `R000009`
16. `draw_line`｜图层 `S_SURFACE`｜源 `E000010 ` → 重绘 `R000010`
17. `draw_line`｜图层 `S_SURFACE`｜源 `E000011 ` → 重绘 `R000011`
18. `draw_line`｜图层 `S_FLOOR`｜源 `E000012 ` → 重绘 `R000012`
19. `draw_polyline`｜图层 `PUB_WALL`｜源 `E000013 ` → 重绘 `R000013`
20. `draw_polyline`｜图层 `S_SURFACE`｜源 `E000014 ` → 重绘 `R000014`
21. `draw_line`｜图层 `S_SURFACE`｜源 `E000015 ` → 重绘 `R000015`
22. `draw_line`｜图层 `S_SURFACE`｜源 `E000016 ` → 重绘 `R000016`
23. `draw_line`｜图层 `S_SURFACE`｜源 `E000017 ` → 重绘 `R000017`
24. `draw_line`｜图层 `S_SURFACE`｜源 `E000019 ` → 重绘 `R000019`
25. `draw_line`｜图层 `S_SURFACE`｜源 `E000020 ` → 重绘 `R000020`
26. `draw_line`｜图层 `PUB_DIM`｜源 `E000022 ` → 重绘 `R000022`
27. `draw_line`｜图层 `S_SURFACE`｜源 `E000024 ` → 重绘 `R000024`
28. `draw_line`｜图层 `S_FLOOR`｜源 `E000025 ` → 重绘 `R000025`
29. `draw_line`｜图层 `S_SURFACE`｜源 `E000027 ` → 重绘 `R000027`
30. `draw_line`｜图层 `PUB_DIM`｜源 `E000028 ` → 重绘 `R000028`
31. `draw_line`｜图层 `PUB_DIM`｜源 `E000029 ` → 重绘 `R000029`
32. `draw_line`｜图层 `PUB_DIM`｜源 `E000030 ` → 重绘 `R000030`
33. `draw_line`｜图层 `S_SURFACE`｜源 `E000032 ` → 重绘 `R000032`
34. `draw_line`｜图层 `S_SURFACE`｜源 `E000033 ` → 重绘 `R000033`
35. `draw_line`｜图层 `S_SURFACE`｜源 `E000034 ` → 重绘 `R000034`
36. `draw_line`｜图层 `S_SURFACE`｜源 `E000036 ` → 重绘 `R000036`
37. `draw_line`｜图层 `S_SURFACE`｜源 `E000038 ` → 重绘 `R000038`
38. `draw_polyline`｜图层 `PUB_WALL`｜源 `E000040 ` → 重绘 `R000040`
39. `draw_line`｜图层 `S_FLOOR`｜源 `E000041 ` → 重绘 `R000041`
40. `draw_line`｜图层 `S_FLOOR`｜源 `E000042 ` → 重绘 `R000042`
41. `draw_line`｜图层 `S_SURFACE`｜源 `E000043 ` → 重绘 `R000043`
42. `draw_line`｜图层 `S_SURFACE`｜源 `E000044 ` → 重绘 `R000044`
43. `draw_polyline`｜图层 `S_SURFACE`｜源 `E000045 ` → 重绘 `R000045`
44. `draw_line`｜图层 `S_FLOOR`｜源 `E000046 ` → 重绘 `R000046`
45. `draw_polyline`｜图层 `S_SURFACE`｜源 `E000047 ` → 重绘 `R000047`
46. `draw_line`｜图层 `S_SURFACE`｜源 `E000048 ` → 重绘 `R000048`
47. `draw_line`｜图层 `S_SURFACE`｜源 `E000049 ` → 重绘 `R000049`
48. `draw_polyline`｜图层 `S_SURFACE`｜源 `E000050 ` → 重绘 `R000050`
49. `draw_line`｜图层 `S_FLOOR`｜源 `E000052 ` → 重绘 `R000052`
50. `draw_line`｜图层 `S_SURFACE`｜源 `E000053 ` → 重绘 `R000053`
51. `draw_arc`｜图层 `S_SURFACE`｜源 `E000054 ` → 重绘 `R000054`
52. `draw_arc`｜图层 `S_SURFACE`｜源 `E000055 ` → 重绘 `R000055`
53. `draw_line`｜图层 `S_SURFACE`｜源 `E000056 ` → 重绘 `R000056`
54. `draw_polyline`｜图层 `S_SURFACE`｜源 `E000057 ` → 重绘 `R000057`
55. `draw_line`｜图层 `PUB_DIM`｜源 `E000062 ` → 重绘 `R000062`
56. `draw_polyline`｜图层 `S_SURFACE`｜源 `E000063 ` → 重绘 `R000063`
57. `draw_line`｜图层 `S_SURFACE`｜源 `E000064 ` → 重绘 `R000064`
58. `draw_line`｜图层 `S_SURFACE`｜源 `E000065 ` → 重绘 `R000065`
59. `draw_polyline`｜图层 `PUB_WALL`｜源 `E000066 ` → 重绘 `R000066`
60. `draw_polyline`｜图层 `PUB_WALL`｜源 `E000067 ` → 重绘 `R000067`
61. `draw_line`｜图层 `S_WALL`｜源 `E000068 ` → 重绘 `R000068`
62. `draw_line`｜图层 `S_WALL`｜源 `E000069 ` → 重绘 `R000069`
63. `hatch`｜图层 `S_SURFACE`｜源 `E000076 ` → 重绘 `R000076`
64. `hatch`｜图层 `S_SURFACE`｜源 `E000077 ` → 重绘 `R000077`
65. `hatch`｜图层 `S_SURFACE`｜源 `E000078 ` → 重绘 `R000078`
66. `draw_polyline`｜图层 `0`｜源 `E000080 ` → 重绘 `R000080`
67. `draw_polyline`｜图层 `0`｜源 `E000081 ` → 重绘 `R000081`
68. `add_text`｜图层 `PUB_TEXT`｜源 `E000002 ` → 重绘 `R000002`
69. `add_text`｜图层 `PUB_TEXT`｜源 `E000003 ` → 重绘 `R000003`
70. `add_text`｜图层 `PUB_TEXT`｜源 `E000018 ` → 重绘 `R000018`
71. `add_text`｜图层 `PUB_TEXT`｜源 `E000021 ` → 重绘 `R000021`
72. `add_text`｜图层 `PUB_TEXT`｜源 `E000023 ` → 重绘 `R000023`
73. `add_text`｜图层 `PUB_TEXT`｜源 `E000026 ` → 重绘 `R000026`
74. `add_text`｜图层 `PUB_TEXT`｜源 `E000031 ` → 重绘 `R000031`
75. `add_text`｜图层 `PUB_TEXT`｜源 `E000035 ` → 重绘 `R000035`
76. `add_text`｜图层 `PUB_TEXT`｜源 `E000037 ` → 重绘 `R000037`
77. `add_text`｜图层 `PUB_TEXT`｜源 `E000039 ` → 重绘 `R000039`
78. `add_text`｜图层 `PUB_TEXT`｜源 `E000051 ` → 重绘 `R000051`
79. `add_text`｜图层 `PUB_TEXT`｜源 `E000058 ` → 重绘 `R000058`
80. `add_text`｜图层 `PUB_TEXT`｜源 `E000059 ` → 重绘 `R000059`
81. `add_text`｜图层 `PUB_TEXT`｜源 `E000070 ` → 重绘 `R000070`
82. `add_text`｜图层 `PUB_TEXT`｜源 `E000079 ` → 重绘 `R000079`
83. `add_text`｜图层 `PUB_TEXT`｜源 `E000082 ` → 重绘 `R000082`
84. `add_dimension`｜图层 `PUB_DIM`｜源 `E000060 ` → 重绘 `R000060`
85. `add_dimension`｜图层 `PUB_DIM`｜源 `E000061 ` → 重绘 `R000061`
86. `add_dimension`｜图层 `PUB_DIM`｜源 `E000071 ` → 重绘 `R000071`
87. `add_dimension`｜图层 `PUB_DIM`｜源 `E000072 ` → 重绘 `R000072`
88. `add_dimension`｜图层 `PUB_DIM`｜源 `E000073 ` → 重绘 `R000073`
89. `add_dimension`｜图层 `PUB_DIM`｜源 `E000074 ` → 重绘 `R000074`
90. `add_dimension`｜图层 `PUB_DIM`｜源 `E000075 ` → 重绘 `R000075`
