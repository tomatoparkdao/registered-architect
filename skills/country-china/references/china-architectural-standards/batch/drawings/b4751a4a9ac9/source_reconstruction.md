# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`DY-柱与侧墙连接处防水大样.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[-6711.4, -10424.31], [22880.9, 1097.18]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `PUB_TEXT`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
4. `draw_line`｜图层 `0`｜源 `E000001 ` → 重绘 `R000001`
5. `draw_line`｜图层 `0`｜源 `E000002 ` → 重绘 `R000002`
6. `draw_polyline`｜图层 `0`｜源 `E000003 ` → 重绘 `R000003`
7. `draw_polyline`｜图层 `0`｜源 `E000004 ` → 重绘 `R000004`
8. `draw_polyline`｜图层 `0`｜源 `E000005 ` → 重绘 `R000005`
9. `draw_polyline`｜图层 `0`｜源 `E000006 ` → 重绘 `R000006`
10. `draw_polyline`｜图层 `0`｜源 `E000007 ` → 重绘 `R000007`
11. `draw_polyline`｜图层 `0`｜源 `E000008 ` → 重绘 `R000008`
12. `draw_line`｜图层 `0`｜源 `E000009 ` → 重绘 `R000009`
13. `draw_polyline`｜图层 `0`｜源 `E000010 ` → 重绘 `R000010`
14. `draw_line`｜图层 `0`｜源 `E000011 ` → 重绘 `R000011`
15. `hatch`｜图层 `0`｜源 `E000012 ` → 重绘 `R000012`
16. `hatch`｜图层 `0`｜源 `E000013 ` → 重绘 `R000013`
17. `hatch`｜图层 `0`｜源 `E000014 ` → 重绘 `R000014`
18. `hatch`｜图层 `0`｜源 `E000015 ` → 重绘 `R000015`
19. `draw_polyline`｜图层 `0`｜源 `E000017 ` → 重绘 `R000017`
20. `draw_polyline`｜图层 `0`｜源 `E000018 ` → 重绘 `R000018`
21. `draw_polyline`｜图层 `0`｜源 `E000019 ` → 重绘 `R000019`
22. `draw_line`｜图层 `PUB_TEXT`｜源 `E000044 ` → 重绘 `R000044`
23. `draw_line`｜图层 `PUB_TEXT`｜源 `E000045 ` → 重绘 `R000045`
24. `draw_line`｜图层 `PUB_TEXT`｜源 `E000046 ` → 重绘 `R000046`
25. `draw_line`｜图层 `PUB_TEXT`｜源 `E000047 ` → 重绘 `R000047`
26. `draw_line`｜图层 `PUB_TEXT`｜源 `E000048 ` → 重绘 `R000048`
27. `draw_line`｜图层 `PUB_TEXT`｜源 `E000049 ` → 重绘 `R000049`
28. `draw_line`｜图层 `PUB_TEXT`｜源 `E000050 ` → 重绘 `R000050`
29. `draw_line`｜图层 `PUB_TEXT`｜源 `E000051 ` → 重绘 `R000051`
30. `draw_line`｜图层 `PUB_TEXT`｜源 `E000052 ` → 重绘 `R000052`
31. `draw_line`｜图层 `PUB_TEXT`｜源 `E000053 ` → 重绘 `R000053`
32. `draw_line`｜图层 `PUB_TEXT`｜源 `E000054 ` → 重绘 `R000054`
33. `draw_line`｜图层 `PUB_TEXT`｜源 `E000055 ` → 重绘 `R000055`
34. `draw_line`｜图层 `PUB_TEXT`｜源 `E000057 ` → 重绘 `R000057`
35. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000062 ` → 重绘 `R000062`
36. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000063 ` → 重绘 `R000063`
37. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000064 ` → 重绘 `R000064`
38. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000065 ` → 重绘 `R000065`
39. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000066 ` → 重绘 `R000066`
40. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000067 ` → 重绘 `R000067`
41. `draw_polyline`｜图层 `0`｜源 `E000068 ` → 重绘 `R000068`
42. `draw_line`｜图层 `0`｜源 `E000069 ` → 重绘 `R000069`
43. `draw_line`｜图层 `0`｜源 `E000070 ` → 重绘 `R000070`
44. `draw_line`｜图层 `0`｜源 `E000071 ` → 重绘 `R000071`
45. `draw_polyline`｜图层 `0`｜源 `E000072 ` → 重绘 `R000072`
46. `draw_line`｜图层 `0`｜源 `E000073 ` → 重绘 `R000073`
47. `draw_polyline`｜图层 `0`｜源 `E000074 ` → 重绘 `R000074`
48. `hatch`｜图层 `PUB_TEXT`｜源 `E000075 ` → 重绘 `R000075`
49. `hatch`｜图层 `PUB_TEXT`｜源 `E000076 ` → 重绘 `R000076`
50. `hatch`｜图层 `PUB_TEXT`｜源 `E000077 ` → 重绘 `R000077`
51. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000078 ` → 重绘 `R000078`
52. `hatch`｜图层 `PUB_TEXT`｜源 `E000079 ` → 重绘 `R000079`
53. `draw_circle`｜图层 `PUB_TEXT`｜源 `E000080 ` → 重绘 `R000080`
54. `hatch`｜图层 `PUB_TEXT`｜源 `E000081 ` → 重绘 `R000081`
55. `draw_circle`｜图层 `PUB_TEXT`｜源 `E000082 ` → 重绘 `R000082`
56. `hatch`｜图层 `PUB_TEXT`｜源 `E000083 ` → 重绘 `R000083`
57. `draw_circle`｜图层 `PUB_TEXT`｜源 `E000084 ` → 重绘 `R000084`
58. `hatch`｜图层 `PUB_TEXT`｜源 `E000085 ` → 重绘 `R000085`
59. `draw_circle`｜图层 `PUB_TEXT`｜源 `E000086 ` → 重绘 `R000086`
60. `hatch`｜图层 `PUB_TEXT`｜源 `E000087 ` → 重绘 `R000087`
61. `draw_circle`｜图层 `PUB_TEXT`｜源 `E000088 ` → 重绘 `R000088`
62. `draw_line`｜图层 `PUB_TEXT`｜源 `E000089 ` → 重绘 `R000089`
63. `draw_line`｜图层 `PUB_TEXT`｜源 `E000090 ` → 重绘 `R000090`
64. `draw_line`｜图层 `PUB_TEXT`｜源 `E000095 ` → 重绘 `R000095`
65. `draw_line`｜图层 `PUB_TEXT`｜源 `E000096 ` → 重绘 `R000096`
66. `draw_line`｜图层 `PUB_TEXT`｜源 `E000114 ` → 重绘 `R000114`
67. `draw_line`｜图层 `PUB_TEXT`｜源 `E000115 ` → 重绘 `R000115`
68. `draw_line`｜图层 `PUB_TEXT`｜源 `E000116 ` → 重绘 `R000116`
69. `draw_line`｜图层 `PUB_TEXT`｜源 `E000117 ` → 重绘 `R000117`
70. `draw_line`｜图层 `PUB_TEXT`｜源 `E000119 ` → 重绘 `R000119`
71. `draw_line`｜图层 `PUB_TEXT`｜源 `E000120 ` → 重绘 `R000120`
72. `draw_line`｜图层 `PUB_TEXT`｜源 `E000121 ` → 重绘 `R000121`
73. `draw_line`｜图层 `PUB_TEXT`｜源 `E000123 ` → 重绘 `R000123`
74. `draw_line`｜图层 `PUB_TEXT`｜源 `E000124 ` → 重绘 `R000124`
75. `draw_line`｜图层 `PUB_TEXT`｜源 `E000125 ` → 重绘 `R000125`
76. `draw_line`｜图层 `PUB_TEXT`｜源 `E000126 ` → 重绘 `R000126`
77. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000129 ` → 重绘 `R000129`
78. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000130 ` → 重绘 `R000130`
79. `add_text`｜图层 `PUB_TEXT`｜源 `E000016 ` → 重绘 `R000016`
80. `add_text`｜图层 `PUB_TEXT`｜源 `E000020 ` → 重绘 `R000020`
81. `add_text`｜图层 `PUB_TEXT`｜源 `E000021 ` → 重绘 `R000021`
82. `add_text`｜图层 `PUB_TEXT`｜源 `E000022 ` → 重绘 `R000022`
83. `add_text`｜图层 `PUB_TEXT`｜源 `E000023 ` → 重绘 `R000023`
84. `add_text`｜图层 `PUB_TEXT`｜源 `E000024 ` → 重绘 `R000024`
85. `add_text`｜图层 `PUB_TEXT`｜源 `E000025 ` → 重绘 `R000025`
86. `add_text`｜图层 `PUB_TEXT`｜源 `E000026 ` → 重绘 `R000026`
87. `add_text`｜图层 `PUB_TEXT`｜源 `E000027 ` → 重绘 `R000027`
88. `add_text`｜图层 `PUB_TEXT`｜源 `E000028 ` → 重绘 `R000028`
89. `add_text`｜图层 `PUB_TEXT`｜源 `E000029 ` → 重绘 `R000029`
90. `add_text`｜图层 `PUB_TEXT`｜源 `E000030 ` → 重绘 `R000030`
91. `add_text`｜图层 `PUB_TEXT`｜源 `E000031 ` → 重绘 `R000031`
92. `add_text`｜图层 `PUB_TEXT`｜源 `E000032 ` → 重绘 `R000032`
93. `add_text`｜图层 `PUB_TEXT`｜源 `E000033 ` → 重绘 `R000033`
94. `add_text`｜图层 `PUB_TEXT`｜源 `E000034 ` → 重绘 `R000034`
95. `add_text`｜图层 `PUB_TEXT`｜源 `E000035 ` → 重绘 `R000035`
96. `add_text`｜图层 `PUB_TEXT`｜源 `E000036 ` → 重绘 `R000036`
97. `add_text`｜图层 `PUB_TEXT`｜源 `E000037 ` → 重绘 `R000037`
98. `add_text`｜图层 `PUB_TEXT`｜源 `E000038 ` → 重绘 `R000038`
99. `add_text`｜图层 `PUB_TEXT`｜源 `E000039 ` → 重绘 `R000039`
100. `add_text`｜图层 `PUB_TEXT`｜源 `E000040 ` → 重绘 `R000040`
101. `add_text`｜图层 `PUB_TEXT`｜源 `E000041 ` → 重绘 `R000041`
102. `add_text`｜图层 `PUB_TEXT`｜源 `E000042 ` → 重绘 `R000042`
103. `add_text`｜图层 `PUB_TEXT`｜源 `E000043 ` → 重绘 `R000043`
104. `add_text`｜图层 `PUB_TEXT`｜源 `E000056 ` → 重绘 `R000056`
105. `add_text`｜图层 `PUB_TEXT`｜源 `E000058 ` → 重绘 `R000058`
106. `add_text`｜图层 `PUB_TEXT`｜源 `E000059 ` → 重绘 `R000059`
107. `add_text`｜图层 `PUB_TEXT`｜源 `E000060 ` → 重绘 `R000060`
108. `add_text`｜图层 `PUB_TEXT`｜源 `E000061 ` → 重绘 `R000061`
109. `add_text`｜图层 `PUB_TEXT`｜源 `E000091 ` → 重绘 `R000091`
110. `add_text`｜图层 `PUB_TEXT`｜源 `E000092 ` → 重绘 `R000092`
111. `add_text`｜图层 `PUB_TEXT`｜源 `E000093 ` → 重绘 `R000093`
112. `add_text`｜图层 `PUB_TEXT`｜源 `E000094 ` → 重绘 `R000094`
113. `add_text`｜图层 `PUB_TEXT`｜源 `E000097 ` → 重绘 `R000097`
114. `add_text`｜图层 `PUB_TEXT`｜源 `E000098 ` → 重绘 `R000098`
115. `add_text`｜图层 `PUB_TEXT`｜源 `E000099 ` → 重绘 `R000099`
116. `add_text`｜图层 `PUB_TEXT`｜源 `E000100 ` → 重绘 `R000100`
117. `add_text`｜图层 `PUB_TEXT`｜源 `E000101 ` → 重绘 `R000101`
118. `add_text`｜图层 `PUB_TEXT`｜源 `E000102 ` → 重绘 `R000102`
119. `add_text`｜图层 `PUB_TEXT`｜源 `E000103 ` → 重绘 `R000103`
120. `add_text`｜图层 `PUB_TEXT`｜源 `E000104 ` → 重绘 `R000104`
121. `add_text`｜图层 `PUB_TEXT`｜源 `E000105 ` → 重绘 `R000105`
122. `add_text`｜图层 `PUB_TEXT`｜源 `E000106 ` → 重绘 `R000106`
123. `add_text`｜图层 `PUB_TEXT`｜源 `E000107 ` → 重绘 `R000107`
124. `add_text`｜图层 `PUB_TEXT`｜源 `E000108 ` → 重绘 `R000108`
125. `add_text`｜图层 `PUB_TEXT`｜源 `E000109 ` → 重绘 `R000109`
126. `add_text`｜图层 `PUB_TEXT`｜源 `E000110 ` → 重绘 `R000110`
127. `add_text`｜图层 `PUB_TEXT`｜源 `E000111 ` → 重绘 `R000111`
128. `add_text`｜图层 `PUB_TEXT`｜源 `E000112 ` → 重绘 `R000112`
129. `add_text`｜图层 `PUB_TEXT`｜源 `E000113 ` → 重绘 `R000113`
130. `add_text`｜图层 `PUB_TEXT`｜源 `E000118 ` → 重绘 `R000118`
131. `add_text`｜图层 `PUB_TEXT`｜源 `E000122 ` → 重绘 `R000122`
132. `add_text`｜图层 `PUB_TEXT`｜源 `E000127 ` → 重绘 `R000127`
133. `add_text`｜图层 `PUB_TEXT`｜源 `E000128 ` → 重绘 `R000128`
134. `add_text`｜图层 `PUB_TEXT`｜源 `E000131 ` → 重绘 `R000131`
135. `add_text`｜图层 `PUB_TEXT`｜源 `E000132 ` → 重绘 `R000132`
136. `add_text`｜图层 `PUB_TEXT`｜源 `E000133 ` → 重绘 `R000133`
137. `add_text`｜图层 `PUB_TEXT`｜源 `E000134 ` → 重绘 `R000134`
138. `add_text`｜图层 `PUB_TEXT`｜源 `E000135 ` → 重绘 `R000135`
139. `add_text`｜图层 `PUB_TEXT`｜源 `E000136 ` → 重绘 `R000136`
140. `add_text`｜图层 `PUB_TEXT`｜源 `E000137 ` → 重绘 `R000137`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
