# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`栏河大样4.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[-110.0, 233.65], [2543.0, 2860.0]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `S_WALL`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `S_DOTE`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `PUB_TEXT`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `E_WALL`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `LM`｜源 `- ` → 重绘 `-`
7. `create_layer`｜图层 `PUB_WALL`｜源 `- ` → 重绘 `-`
8. `create_layer`｜图层 `PUB_DIM`｜源 `- ` → 重绘 `-`
9. `create_layer`｜图层 `DEFPOINTS`｜源 `- ` → 重绘 `-`
10. `create_layer`｜图层 `S_OTHER`｜源 `- ` → 重绘 `-`
11. `create_layer`｜图层 `DOTE`｜源 `- ` → 重绘 `-`
12. `create_layer`｜图层 `WALL`｜源 `- ` → 重绘 `-`
13. `create_layer`｜图层 `WINDOW`｜源 `- ` → 重绘 `-`
14. `create_layer`｜图层 `WINDOW_TEXT`｜源 `- ` → 重绘 `-`
15. `create_layer`｜图层 `OTHER`｜源 `- ` → 重绘 `-`
16. `create_layer`｜图层 `S_E_FLOOR`｜源 `- ` → 重绘 `-`
17. `create_layer`｜图层 `S_SURFACE`｜源 `- ` → 重绘 `-`
18. `create_layer`｜图层 `PUB_HATCH`｜源 `- ` → 重绘 `-`
19. `create_layer`｜图层 `S_FLOOR`｜源 `- ` → 重绘 `-`
20. `create_layer`｜图层 `S_E_COLUMN`｜源 `- ` → 重绘 `-`
21. `draw_polyline`｜图层 `LM`｜源 `E000002 ` → 重绘 `R000002`
22. `draw_polyline`｜图层 `LM`｜源 `E000003 ` → 重绘 `R000003`
23. `draw_line`｜图层 `PUB_DIM`｜源 `E000005 ` → 重绘 `R000005`
24. `draw_line`｜图层 `PUB_DIM`｜源 `E000006 ` → 重绘 `R000006`
25. `draw_line`｜图层 `PUB_DIM`｜源 `E000007 ` → 重绘 `R000007`
26. `draw_line`｜图层 `PUB_DIM`｜源 `E000008 ` → 重绘 `R000008`
27. `draw_line`｜图层 `PUB_DIM`｜源 `E000009 ` → 重绘 `R000009`
28. `draw_line`｜图层 `S_DOTE`｜源 `E000013 ` → 重绘 `R000013`
29. `draw_line`｜图层 `LM`｜源 `E000026 ` → 重绘 `R000026`
30. `draw_line`｜图层 `LM`｜源 `E000027 ` → 重绘 `R000027`
31. `draw_line`｜图层 `LM`｜源 `E000028 ` → 重绘 `R000028`
32. `draw_line`｜图层 `LM`｜源 `E000029 ` → 重绘 `R000029`
33. `draw_line`｜图层 `LM`｜源 `E000030 ` → 重绘 `R000030`
34. `draw_line`｜图层 `LM`｜源 `E000031 ` → 重绘 `R000031`
35. `draw_line`｜图层 `LM`｜源 `E000032 ` → 重绘 `R000032`
36. `draw_line`｜图层 `LM`｜源 `E000033 ` → 重绘 `R000033`
37. `draw_line`｜图层 `LM`｜源 `E000034 ` → 重绘 `R000034`
38. `draw_line`｜图层 `LM`｜源 `E000035 ` → 重绘 `R000035`
39. `draw_line`｜图层 `LM`｜源 `E000036 ` → 重绘 `R000036`
40. `draw_line`｜图层 `LM`｜源 `E000038 ` → 重绘 `R000038`
41. `draw_line`｜图层 `LM`｜源 `E000039 ` → 重绘 `R000039`
42. `draw_line`｜图层 `LM`｜源 `E000040 ` → 重绘 `R000040`
43. `draw_line`｜图层 `LM`｜源 `E000041 ` → 重绘 `R000041`
44. `draw_line`｜图层 `LM`｜源 `E000042 ` → 重绘 `R000042`
45. `draw_line`｜图层 `LM`｜源 `E000043 ` → 重绘 `R000043`
46. `draw_line`｜图层 `LM`｜源 `E000044 ` → 重绘 `R000044`
47. `draw_line`｜图层 `LM`｜源 `E000045 ` → 重绘 `R000045`
48. `draw_line`｜图层 `LM`｜源 `E000046 ` → 重绘 `R000046`
49. `draw_line`｜图层 `LM`｜源 `E000047 ` → 重绘 `R000047`
50. `draw_line`｜图层 `S_SURFACE`｜源 `E000048 ` → 重绘 `R000048`
51. `draw_line`｜图层 `S_SURFACE`｜源 `E000049 ` → 重绘 `R000049`
52. `draw_line`｜图层 `S_SURFACE`｜源 `E000050 ` → 重绘 `R000050`
53. `draw_line`｜图层 `S_SURFACE`｜源 `E000051 ` → 重绘 `R000051`
54. `draw_line`｜图层 `S_SURFACE`｜源 `E000052 ` → 重绘 `R000052`
55. `draw_line`｜图层 `S_SURFACE`｜源 `E000053 ` → 重绘 `R000053`
56. `draw_line`｜图层 `S_SURFACE`｜源 `E000054 ` → 重绘 `R000054`
57. `draw_line`｜图层 `S_SURFACE`｜源 `E000055 ` → 重绘 `R000055`
58. `draw_line`｜图层 `S_SURFACE`｜源 `E000056 ` → 重绘 `R000056`
59. `draw_line`｜图层 `S_SURFACE`｜源 `E000057 ` → 重绘 `R000057`
60. `draw_line`｜图层 `LM`｜源 `E000058 ` → 重绘 `R000058`
61. `draw_polyline`｜图层 `LM`｜源 `E000059 ` → 重绘 `R000059`
62. `draw_polyline`｜图层 `PUB_DIM`｜源 `E000071 ` → 重绘 `R000071`
63. `insert_block`｜图层 `PUB_DIM`｜源 `E000072 ` → 重绘 `R000072`
64. `insert_block`｜图层 `PUB_DIM`｜源 `E000075 ` → 重绘 `R000075`
65. `draw_polyline`｜图层 `PUB_DIM`｜源 `E000076 ` → 重绘 `R000076`
66. `draw_line`｜图层 `S_SURFACE`｜源 `E000079 ` → 重绘 `R000079`
67. `draw_line`｜图层 `S_SURFACE`｜源 `E000080 ` → 重绘 `R000080`
68. `draw_line`｜图层 `S_SURFACE`｜源 `E000081 ` → 重绘 `R000081`
69. `draw_line`｜图层 `S_SURFACE`｜源 `E000082 ` → 重绘 `R000082`
70. `draw_line`｜图层 `S_SURFACE`｜源 `E000083 ` → 重绘 `R000083`
71. `draw_arc`｜图层 `S_SURFACE`｜源 `E000084 ` → 重绘 `R000084`
72. `draw_arc`｜图层 `S_SURFACE`｜源 `E000085 ` → 重绘 `R000085`
73. `draw_arc`｜图层 `S_SURFACE`｜源 `E000086 ` → 重绘 `R000086`
74. `draw_arc`｜图层 `S_SURFACE`｜源 `E000087 ` → 重绘 `R000087`
75. `draw_arc`｜图层 `S_SURFACE`｜源 `E000088 ` → 重绘 `R000088`
76. `draw_arc`｜图层 `S_SURFACE`｜源 `E000089 ` → 重绘 `R000089`
77. `draw_line`｜图层 `LM`｜源 `E000090 ` → 重绘 `R000090`
78. `draw_line`｜图层 `LM`｜源 `E000091 ` → 重绘 `R000091`
79. `hatch`｜图层 `LM`｜源 `E000093 ` → 重绘 `R000093`
80. `draw_line`｜图层 `S_WALL`｜源 `E000094 ` → 重绘 `R000094`
81. `draw_line`｜图层 `S_WALL`｜源 `E000095 ` → 重绘 `R000095`
82. `draw_line`｜图层 `S_WALL`｜源 `E000096 ` → 重绘 `R000096`
83. `draw_line`｜图层 `S_WALL`｜源 `E000097 ` → 重绘 `R000097`
84. `draw_line`｜图层 `S_WALL`｜源 `E000098 ` → 重绘 `R000098`
85. `draw_line`｜图层 `S_WALL`｜源 `E000099 ` → 重绘 `R000099`
86. `draw_line`｜图层 `S_WALL`｜源 `E000100 ` → 重绘 `R000100`
87. `draw_line`｜图层 `S_WALL`｜源 `E000101 ` → 重绘 `R000101`
88. `draw_line`｜图层 `S_WALL`｜源 `E000102 ` → 重绘 `R000102`
89. `draw_line`｜图层 `S_WALL`｜源 `E000103 ` → 重绘 `R000103`
90. `draw_line`｜图层 `S_WALL`｜源 `E000104 ` → 重绘 `R000104`
91. `draw_line`｜图层 `S_WALL`｜源 `E000105 ` → 重绘 `R000105`
92. `draw_line`｜图层 `S_WALL`｜源 `E000106 ` → 重绘 `R000106`
93. `draw_line`｜图层 `S_WALL`｜源 `E000107 ` → 重绘 `R000107`
94. `draw_line`｜图层 `S_WALL`｜源 `E000108 ` → 重绘 `R000108`
95. `draw_line`｜图层 `S_WALL`｜源 `E000109 ` → 重绘 `R000109`
96. `draw_polyline`｜图层 `PUB_WALL`｜源 `E000110 ` → 重绘 `R000110`
97. `draw_polyline`｜图层 `PUB_WALL`｜源 `E000111 ` → 重绘 `R000111`
98. `draw_polyline`｜图层 `PUB_WALL`｜源 `E000112 ` → 重绘 `R000112`
99. `add_text`｜图层 `PUB_TEXT`｜源 `E000001 ` → 重绘 `R000001`
100. `add_text`｜图层 `PUB_TEXT`｜源 `E000004 ` → 重绘 `R000004`
101. `add_text`｜图层 `PUB_TEXT`｜源 `E000037 ` → 重绘 `R000037`
102. `add_text`｜图层 `PUB_TEXT`｜源 `E000060 ` → 重绘 `R000060`
103. `add_text`｜图层 `PUB_TEXT`｜源 `E000061 ` → 重绘 `R000061`
104. `add_text`｜图层 `PUB_TEXT`｜源 `E000062 ` → 重绘 `R000062`
105. `add_text`｜图层 `PUB_TEXT`｜源 `E000063 ` → 重绘 `R000063`
106. `add_text`｜图层 `PUB_TEXT`｜源 `E000064 ` → 重绘 `R000064`
107. `add_text`｜图层 `PUB_TEXT`｜源 `E000065 ` → 重绘 `R000065`
108. `add_text`｜图层 `PUB_TEXT`｜源 `E000066 ` → 重绘 `R000066`
109. `add_text`｜图层 `PUB_TEXT`｜源 `E000067 ` → 重绘 `R000067`
110. `add_text`｜图层 `PUB_TEXT`｜源 `E000068 ` → 重绘 `R000068`
111. `add_text`｜图层 `PUB_TEXT`｜源 `E000069 ` → 重绘 `R000069`
112. `add_text`｜图层 `PUB_TEXT`｜源 `E000070 ` → 重绘 `R000070`
113. `add_text`｜图层 `PUB_TEXT`｜源 `E000073 ` → 重绘 `R000073`
114. `add_text`｜图层 `PUB_TEXT`｜源 `E000074 ` → 重绘 `R000074`
115. `add_text`｜图层 `PUB_TEXT`｜源 `E000077 ` → 重绘 `R000077`
116. `add_text`｜图层 `PUB_TEXT`｜源 `E000078 ` → 重绘 `R000078`
117. `add_dimension`｜图层 `PUB_DIM`｜源 `E000010 ` → 重绘 `R000010`
118. `add_dimension`｜图层 `PUB_DIM`｜源 `E000011 ` → 重绘 `R000011`
119. `add_dimension`｜图层 `PUB_DIM`｜源 `E000012 ` → 重绘 `R000012`
120. `add_dimension`｜图层 `PUB_DIM`｜源 `E000014 ` → 重绘 `R000014`
121. `add_dimension`｜图层 `PUB_DIM`｜源 `E000015 ` → 重绘 `R000015`
122. `add_dimension`｜图层 `PUB_DIM`｜源 `E000016 ` → 重绘 `R000016`
123. `add_dimension`｜图层 `PUB_DIM`｜源 `E000017 ` → 重绘 `R000017`
124. `add_dimension`｜图层 `PUB_DIM`｜源 `E000018 ` → 重绘 `R000018`
125. `add_dimension`｜图层 `PUB_DIM`｜源 `E000019 ` → 重绘 `R000019`
126. `add_dimension`｜图层 `PUB_DIM`｜源 `E000020 ` → 重绘 `R000020`
127. `add_dimension`｜图层 `PUB_DIM`｜源 `E000021 ` → 重绘 `R000021`
128. `add_dimension`｜图层 `PUB_DIM`｜源 `E000022 ` → 重绘 `R000022`
129. `add_dimension`｜图层 `PUB_DIM`｜源 `E000023 ` → 重绘 `R000023`
130. `add_dimension`｜图层 `PUB_DIM`｜源 `E000024 ` → 重绘 `R000024`
131. `add_dimension`｜图层 `PUB_DIM`｜源 `E000025 ` → 重绘 `R000025`
132. `add_dimension`｜图层 `PUB_DIM`｜源 `E000092 ` → 重绘 `R000092`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
