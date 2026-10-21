# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`DY-屋面防水作法.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[9960.58, 10280.24], [11924.43, 11862.87]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `PUB_TEXT`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `PUB_DIM`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `DEFPOINTS`｜源 `- ` → 重绘 `-`
5. `draw_polyline`｜图层 `0`｜源 `E000001 ` → 重绘 `R000001`
6. `draw_polyline`｜图层 `0`｜源 `E000002 ` → 重绘 `R000002`
7. `draw_polyline`｜图层 `0`｜源 `E000003 ` → 重绘 `R000003`
8. `draw_polyline`｜图层 `0`｜源 `E000004 ` → 重绘 `R000004`
9. `draw_polyline`｜图层 `0`｜源 `E000005 ` → 重绘 `R000005`
10. `draw_polyline`｜图层 `0`｜源 `E000006 ` → 重绘 `R000006`
11. `draw_polyline`｜图层 `0`｜源 `E000007 ` → 重绘 `R000007`
12. `draw_polyline`｜图层 `0`｜源 `E000008 ` → 重绘 `R000008`
13. `draw_polyline`｜图层 `0`｜源 `E000009 ` → 重绘 `R000009`
14. `draw_polyline`｜图层 `0`｜源 `E000010 ` → 重绘 `R000010`
15. `draw_polyline`｜图层 `0`｜源 `E000011 ` → 重绘 `R000011`
16. `hatch`｜图层 `0`｜源 `E000012 ` → 重绘 `R000012`
17. `draw_polyline`｜图层 `0`｜源 `E000013 ` → 重绘 `R000013`
18. `draw_polyline`｜图层 `0`｜源 `E000014 ` → 重绘 `R000014`
19. `draw_polyline`｜图层 `0`｜源 `E000015 ` → 重绘 `R000015`
20. `draw_polyline`｜图层 `0`｜源 `E000016 ` → 重绘 `R000016`
21. `draw_polyline`｜图层 `0`｜源 `E000017 ` → 重绘 `R000017`
22. `draw_line`｜图层 `0`｜源 `E000018 ` → 重绘 `R000018`
23. `draw_polyline`｜图层 `0`｜源 `E000019 ` → 重绘 `R000019`
24. `draw_polyline`｜图层 `0`｜源 `E000020 ` → 重绘 `R000020`
25. `draw_polyline`｜图层 `0`｜源 `E000021 ` → 重绘 `R000021`
26. `draw_polyline`｜图层 `0`｜源 `E000022 ` → 重绘 `R000022`
27. `draw_polyline`｜图层 `0`｜源 `E000023 ` → 重绘 `R000023`
28. `draw_line`｜图层 `0`｜源 `E000024 ` → 重绘 `R000024`
29. `draw_polyline`｜图层 `0`｜源 `E000025 ` → 重绘 `R000025`
30. `draw_polyline`｜图层 `0`｜源 `E000026 ` → 重绘 `R000026`
31. `draw_polyline`｜图层 `0`｜源 `E000027 ` → 重绘 `R000027`
32. `draw_polyline`｜图层 `0`｜源 `E000028 ` → 重绘 `R000028`
33. `draw_polyline`｜图层 `0`｜源 `E000029 ` → 重绘 `R000029`
34. `draw_polyline`｜图层 `0`｜源 `E000030 ` → 重绘 `R000030`
35. `hatch`｜图层 `0`｜源 `E000031 ` → 重绘 `R000031`
36. `draw_polyline`｜图层 `0`｜源 `E000032 ` → 重绘 `R000032`
37. `draw_polyline`｜图层 `0`｜源 `E000033 ` → 重绘 `R000033`
38. `draw_polyline`｜图层 `0`｜源 `E000034 ` → 重绘 `R000034`
39. `draw_polyline`｜图层 `0`｜源 `E000035 ` → 重绘 `R000035`
40. `draw_polyline`｜图层 `0`｜源 `E000036 ` → 重绘 `R000036`
41. `draw_polyline`｜图层 `0`｜源 `E000037 ` → 重绘 `R000037`
42. `draw_polyline`｜图层 `0`｜源 `E000038 ` → 重绘 `R000038`
43. `draw_polyline`｜图层 `0`｜源 `E000039 ` → 重绘 `R000039`
44. `draw_polyline`｜图层 `0`｜源 `E000040 ` → 重绘 `R000040`
45. `draw_polyline`｜图层 `0`｜源 `E000041 ` → 重绘 `R000041`
46. `draw_polyline`｜图层 `0`｜源 `E000042 ` → 重绘 `R000042`
47. `draw_polyline`｜图层 `0`｜源 `E000043 ` → 重绘 `R000043`
48. `hatch`｜图层 `0`｜源 `E000044 ` → 重绘 `R000044`
49. `hatch`｜图层 `0`｜源 `E000045 ` → 重绘 `R000045`
50. `draw_polyline`｜图层 `0`｜源 `E000046 ` → 重绘 `R000046`
51. `draw_polyline`｜图层 `0`｜源 `E000047 ` → 重绘 `R000047`
52. `draw_polyline`｜图层 `0`｜源 `E000048 ` → 重绘 `R000048`
53. `draw_polyline`｜图层 `0`｜源 `E000049 ` → 重绘 `R000049`
54. `hatch`｜图层 `0`｜源 `E000050 ` → 重绘 `R000050`
55. `hatch`｜图层 `0`｜源 `E000051 ` → 重绘 `R000051`
56. `hatch`｜图层 `0`｜源 `E000052 ` → 重绘 `R000052`
57. `hatch`｜图层 `0`｜源 `E000053 ` → 重绘 `R000053`
58. `hatch`｜图层 `0`｜源 `E000054 ` → 重绘 `R000054`
59. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000056 ` → 重绘 `R000056`
60. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000057 ` → 重绘 `R000057`
61. `draw_line`｜图层 `0`｜源 `E000063 ` → 重绘 `R000063`
62. `draw_line`｜图层 `0`｜源 `E000064 ` → 重绘 `R000064`
63. `draw_line`｜图层 `PUB_TEXT`｜源 `E000065 ` → 重绘 `R000065`
64. `draw_line`｜图层 `PUB_TEXT`｜源 `E000066 ` → 重绘 `R000066`
65. `draw_line`｜图层 `PUB_TEXT`｜源 `E000069 ` → 重绘 `R000069`
66. `draw_line`｜图层 `PUB_TEXT`｜源 `E000070 ` → 重绘 `R000070`
67. `draw_line`｜图层 `0`｜源 `E000075 ` → 重绘 `R000075`
68. `draw_line`｜图层 `0`｜源 `E000076 ` → 重绘 `R000076`
69. `draw_line`｜图层 `0`｜源 `E000077 ` → 重绘 `R000077`
70. `draw_line`｜图层 `0`｜源 `E000078 ` → 重绘 `R000078`
71. `draw_line`｜图层 `PUB_TEXT`｜源 `E000080 ` → 重绘 `R000080`
72. `draw_line`｜图层 `PUB_TEXT`｜源 `E000081 ` → 重绘 `R000081`
73. `draw_line`｜图层 `PUB_TEXT`｜源 `E000089 ` → 重绘 `R000089`
74. `draw_line`｜图层 `PUB_TEXT`｜源 `E000090 ` → 重绘 `R000090`
75. `draw_line`｜图层 `PUB_TEXT`｜源 `E000094 ` → 重绘 `R000094`
76. `draw_line`｜图层 `0`｜源 `E000095 ` → 重绘 `R000095`
77. `draw_line`｜图层 `PUB_TEXT`｜源 `E000096 ` → 重绘 `R000096`
78. `draw_line`｜图层 `PUB_TEXT`｜源 `E000097 ` → 重绘 `R000097`
79. `draw_line`｜图层 `PUB_TEXT`｜源 `E000101 ` → 重绘 `R000101`
80. `draw_line`｜图层 `PUB_TEXT`｜源 `E000102 ` → 重绘 `R000102`
81. `add_text`｜图层 `PUB_TEXT`｜源 `E000055 ` → 重绘 `R000055`
82. `add_text`｜图层 `PUB_TEXT`｜源 `E000067 ` → 重绘 `R000067`
83. `add_text`｜图层 `PUB_TEXT`｜源 `E000068 ` → 重绘 `R000068`
84. `add_text`｜图层 `PUB_TEXT`｜源 `E000071 ` → 重绘 `R000071`
85. `add_text`｜图层 `PUB_TEXT`｜源 `E000072 ` → 重绘 `R000072`
86. `add_text`｜图层 `PUB_TEXT`｜源 `E000073 ` → 重绘 `R000073`
87. `add_text`｜图层 `PUB_TEXT`｜源 `E000074 ` → 重绘 `R000074`
88. `add_text`｜图层 `PUB_TEXT`｜源 `E000082 ` → 重绘 `R000082`
89. `add_text`｜图层 `PUB_TEXT`｜源 `E000083 ` → 重绘 `R000083`
90. `add_text`｜图层 `PUB_TEXT`｜源 `E000084 ` → 重绘 `R000084`
91. `add_text`｜图层 `PUB_TEXT`｜源 `E000085 ` → 重绘 `R000085`
92. `add_text`｜图层 `PUB_TEXT`｜源 `E000086 ` → 重绘 `R000086`
93. `add_text`｜图层 `PUB_TEXT`｜源 `E000087 ` → 重绘 `R000087`
94. `add_text`｜图层 `PUB_TEXT`｜源 `E000088 ` → 重绘 `R000088`
95. `add_text`｜图层 `PUB_TEXT`｜源 `E000091 ` → 重绘 `R000091`
96. `add_text`｜图层 `PUB_TEXT`｜源 `E000092 ` → 重绘 `R000092`
97. `add_text`｜图层 `PUB_TEXT`｜源 `E000093 ` → 重绘 `R000093`
98. `add_text`｜图层 `PUB_TEXT`｜源 `E000098 ` → 重绘 `R000098`
99. `add_text`｜图层 `PUB_TEXT`｜源 `E000099 ` → 重绘 `R000099`
100. `add_text`｜图层 `PUB_TEXT`｜源 `E000100 ` → 重绘 `R000100`
101. `add_text`｜图层 `PUB_TEXT`｜源 `E000103 ` → 重绘 `R000103`
102. `add_text`｜图层 `PUB_TEXT`｜源 `E000104 ` → 重绘 `R000104`
103. `add_text`｜图层 `PUB_TEXT`｜源 `E000105 ` → 重绘 `R000105`
104. `add_text`｜图层 `PUB_TEXT`｜源 `E000106 ` → 重绘 `R000106`
105. `add_dimension`｜图层 `PUB_DIM`｜源 `E000058 ` → 重绘 `R000058`
106. `add_dimension`｜图层 `PUB_DIM`｜源 `E000059 ` → 重绘 `R000059`
107. `add_dimension`｜图层 `PUB_DIM`｜源 `E000060 ` → 重绘 `R000060`
108. `add_dimension`｜图层 `PUB_DIM`｜源 `E000061 ` → 重绘 `R000061`
109. `add_dimension`｜图层 `PUB_DIM`｜源 `E000062 ` → 重绘 `R000062`
110. `add_dimension`｜图层 `PUB_DIM`｜源 `E000079 ` → 重绘 `R000079`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
