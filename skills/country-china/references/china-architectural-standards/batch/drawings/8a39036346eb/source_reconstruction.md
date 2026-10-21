# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`分仓缝.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[3156.96, 89.44], [4105.98, 1654.28]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `WALL`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `DIM`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `DEFPOINTS`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `A-DIM`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `ZXX`｜源 `- ` → 重绘 `-`
7. `create_layer`｜图层 `TEXT`｜源 `- ` → 重绘 `-`
8. `create_layer`｜图层 `PUB_TEXT`｜源 `- ` → 重绘 `-`
9. `create_layer`｜图层 `A`｜源 `- ` → 重绘 `-`
10. `create_layer`｜图层 `S`｜源 `- ` → 重绘 `-`
11. `create_layer`｜图层 `H`｜源 `- ` → 重绘 `-`
12. `create_layer`｜图层 `DIM2`｜源 `- ` → 重绘 `-`
13. `create_layer`｜图层 `COLUMN`｜源 `- ` → 重绘 `-`
14. `draw_polyline`｜图层 `A-DIM`｜源 `E000001 ` → 重绘 `R000001`
15. `draw_polyline`｜图层 `A-DIM`｜源 `E000002 ` → 重绘 `R000002`
16. `draw_polyline`｜图层 `A-DIM`｜源 `E000003 ` → 重绘 `R000003`
17. `draw_line`｜图层 `TEXT`｜源 `E000005 ` → 重绘 `R000005`
18. `draw_polyline`｜图层 `DIM`｜源 `E000006 ` → 重绘 `R000006`
19. `draw_line`｜图层 `S`｜源 `E000007 ` → 重绘 `R000007`
20. `draw_line`｜图层 `S`｜源 `E000008 ` → 重绘 `R000008`
21. `draw_line`｜图层 `TEXT`｜源 `E000013 ` → 重绘 `R000013`
22. `draw_polyline`｜图层 `H`｜源 `E000014 ` → 重绘 `R000014`
23. `draw_line`｜图层 `A`｜源 `E000015 ` → 重绘 `R000015`
24. `draw_line`｜图层 `TEXT`｜源 `E000022 ` → 重绘 `R000022`
25. `draw_line`｜图层 `TEXT`｜源 `E000023 ` → 重绘 `R000023`
26. `draw_line`｜图层 `TEXT`｜源 `E000024 ` → 重绘 `R000024`
27. `draw_line`｜图层 `TEXT`｜源 `E000027 ` → 重绘 `R000027`
28. `draw_line`｜图层 `TEXT`｜源 `E000028 ` → 重绘 `R000028`
29. `draw_line`｜图层 `TEXT`｜源 `E000032 ` → 重绘 `R000032`
30. `draw_polyline`｜图层 `DIM`｜源 `E000035 ` → 重绘 `R000035`
31. `draw_line`｜图层 `S`｜源 `E000036 ` → 重绘 `R000036`
32. `draw_line`｜图层 `S`｜源 `E000037 ` → 重绘 `R000037`
33. `draw_line`｜图层 `TEXT`｜源 `E000039 ` → 重绘 `R000039`
34. `draw_line`｜图层 `A`｜源 `E000040 ` → 重绘 `R000040`
35. `draw_line`｜图层 `A`｜源 `E000041 ` → 重绘 `R000041`
36. `draw_line`｜图层 `TEXT`｜源 `E000044 ` → 重绘 `R000044`
37. `draw_line`｜图层 `TEXT`｜源 `E000045 ` → 重绘 `R000045`
38. `draw_line`｜图层 `TEXT`｜源 `E000046 ` → 重绘 `R000046`
39. `draw_polyline`｜图层 `H`｜源 `E000047 ` → 重绘 `R000047`
40. `draw_line`｜图层 `A`｜源 `E000048 ` → 重绘 `R000048`
41. `hatch`｜图层 `H`｜源 `E000049 ` → 重绘 `R000049`
42. `draw_line`｜图层 `A`｜源 `E000050 ` → 重绘 `R000050`
43. `draw_line`｜图层 `TEXT`｜源 `E000055 ` → 重绘 `R000055`
44. `draw_line`｜图层 `TEXT`｜源 `E000058 ` → 重绘 `R000058`
45. `draw_line`｜图层 `TEXT`｜源 `E000059 ` → 重绘 `R000059`
46. `draw_circle`｜图层 `PUB_TEXT`｜源 `E000060 ` → 重绘 `R000060`
47. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000061 ` → 重绘 `R000061`
48. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000062 ` → 重绘 `R000062`
49. `hatch`｜图层 `H`｜源 `E000065 ` → 重绘 `R000065`
50. `hatch`｜图层 `H`｜源 `E000066 ` → 重绘 `R000066`
51. `draw_polyline`｜图层 `DIM`｜源 `E000067 ` → 重绘 `R000067`
52. `hatch`｜图层 `H`｜源 `E000068 ` → 重绘 `R000068`
53. `hatch`｜图层 `H`｜源 `E000069 ` → 重绘 `R000069`
54. `hatch`｜图层 `H`｜源 `E000070 ` → 重绘 `R000070`
55. `hatch`｜图层 `H`｜源 `E000071 ` → 重绘 `R000071`
56. `hatch`｜图层 `H`｜源 `E000072 ` → 重绘 `R000072`
57. `draw_line`｜图层 `A`｜源 `E000073 ` → 重绘 `R000073`
58. `draw_line`｜图层 `A`｜源 `E000074 ` → 重绘 `R000074`
59. `draw_line`｜图层 `A`｜源 `E000075 ` → 重绘 `R000075`
60. `draw_line`｜图层 `A`｜源 `E000076 ` → 重绘 `R000076`
61. `draw_line`｜图层 `A`｜源 `E000077 ` → 重绘 `R000077`
62. `draw_polyline`｜图层 `H`｜源 `E000078 ` → 重绘 `R000078`
63. `draw_polyline`｜图层 `H`｜源 `E000079 ` → 重绘 `R000079`
64. `draw_line`｜图层 `S`｜源 `E000080 ` → 重绘 `R000080`
65. `draw_line`｜图层 `A`｜源 `E000081 ` → 重绘 `R000081`
66. `hatch`｜图层 `H`｜源 `E000082 ` → 重绘 `R000082`
67. `hatch`｜图层 `COLUMN`｜源 `E000083 ` → 重绘 `R000083`
68. `draw_polyline`｜图层 `A`｜源 `E000084 ` → 重绘 `R000084`
69. `draw_line`｜图层 `A`｜源 `E000085 ` → 重绘 `R000085`
70. `add_text`｜图层 `TEXT`｜源 `E000004 ` → 重绘 `R000004`
71. `add_text`｜图层 `TEXT`｜源 `E000009 ` → 重绘 `R000009`
72. `add_text`｜图层 `TEXT`｜源 `E000010 ` → 重绘 `R000010`
73. `add_text`｜图层 `TEXT`｜源 `E000011 ` → 重绘 `R000011`
74. `add_text`｜图层 `TEXT`｜源 `E000012 ` → 重绘 `R000012`
75. `add_text`｜图层 `TEXT`｜源 `E000016 ` → 重绘 `R000016`
76. `add_text`｜图层 `TEXT`｜源 `E000017 ` → 重绘 `R000017`
77. `add_text`｜图层 `TEXT`｜源 `E000018 ` → 重绘 `R000018`
78. `add_text`｜图层 `TEXT`｜源 `E000019 ` → 重绘 `R000019`
79. `add_text`｜图层 `TEXT`｜源 `E000020 ` → 重绘 `R000020`
80. `add_text`｜图层 `TEXT`｜源 `E000021 ` → 重绘 `R000021`
81. `add_text`｜图层 `TEXT`｜源 `E000025 ` → 重绘 `R000025`
82. `add_text`｜图层 `TEXT`｜源 `E000026 ` → 重绘 `R000026`
83. `add_text`｜图层 `TEXT`｜源 `E000029 ` → 重绘 `R000029`
84. `add_text`｜图层 `TEXT`｜源 `E000030 ` → 重绘 `R000030`
85. `add_text`｜图层 `TEXT`｜源 `E000031 ` → 重绘 `R000031`
86. `add_text`｜图层 `TEXT`｜源 `E000033 ` → 重绘 `R000033`
87. `add_text`｜图层 `TEXT`｜源 `E000034 ` → 重绘 `R000034`
88. `add_text`｜图层 `TEXT`｜源 `E000038 ` → 重绘 `R000038`
89. `add_text`｜图层 `TEXT`｜源 `E000042 ` → 重绘 `R000042`
90. `add_text`｜图层 `TEXT`｜源 `E000051 ` → 重绘 `R000051`
91. `add_text`｜图层 `TEXT`｜源 `E000052 ` → 重绘 `R000052`
92. `add_text`｜图层 `TEXT`｜源 `E000053 ` → 重绘 `R000053`
93. `add_text`｜图层 `TEXT`｜源 `E000054 ` → 重绘 `R000054`
94. `add_text`｜图层 `TEXT`｜源 `E000056 ` → 重绘 `R000056`
95. `add_text`｜图层 `TEXT`｜源 `E000057 ` → 重绘 `R000057`
96. `add_text`｜图层 `PUB_TEXT`｜源 `E000063 ` → 重绘 `R000063`
97. `add_text`｜图层 `TEXT`｜源 `E000064 ` → 重绘 `R000064`
98. `add_dimension`｜图层 `DIM2`｜源 `E000043 ` → 重绘 `R000043`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
