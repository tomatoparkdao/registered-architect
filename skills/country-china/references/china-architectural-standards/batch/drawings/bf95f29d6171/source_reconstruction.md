# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`标准运动场.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[-156558.0, -87658.0], [154767.12, 87658.0]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `DOTE`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `PUB_TEXT`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `WALL1`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `OUTLINE`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `WALL`｜源 `- ` → 重绘 `-`
7. `create_layer`｜图层 ``｜源 `- ` → 重绘 `-`
8. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
9. `draw_line`｜图层 `WALL1`｜源 `E000001 ` → 重绘 `R000001`
10. `draw_line`｜图层 `WALL1`｜源 `E000002 ` → 重绘 `R000002`
11. `draw_arc`｜图层 `OUTLINE`｜源 `E000003 ` → 重绘 `R000003`
12. `draw_arc`｜图层 `OUTLINE`｜源 `E000004 ` → 重绘 `R000004`
13. `draw_arc`｜图层 `OUTLINE`｜源 `E000005 ` → 重绘 `R000005`
14. `draw_arc`｜图层 `OUTLINE`｜源 `E000006 ` → 重绘 `R000006`
15. `draw_line`｜图层 `DOTE`｜源 `E000007 ` → 重绘 `R000007`
16. `draw_line`｜图层 `DOTE`｜源 `E000008 ` → 重绘 `R000008`
17. `draw_line`｜图层 `DOTE`｜源 `E000009 ` → 重绘 `R000009`
18. `draw_line`｜图层 `WALL1`｜源 `E000010 ` → 重绘 `R000010`
19. `draw_line`｜图层 `OUTLINE`｜源 `E000011 ` → 重绘 `R000011`
20. `draw_line`｜图层 `OUTLINE`｜源 `E000012 ` → 重绘 `R000012`
21. `draw_line`｜图层 `OUTLINE`｜源 `E000013 ` → 重绘 `R000013`
22. `draw_line`｜图层 `OUTLINE`｜源 `E000014 ` → 重绘 `R000014`
23. `draw_line`｜图层 `OUTLINE`｜源 `E000015 ` → 重绘 `R000015`
24. `draw_arc`｜图层 `OUTLINE`｜源 `E000016 ` → 重绘 `R000016`
25. `draw_line`｜图层 `OUTLINE`｜源 `E000017 ` → 重绘 `R000017`
26. `draw_line`｜图层 `OUTLINE`｜源 `E000018 ` → 重绘 `R000018`
27. `draw_line`｜图层 `OUTLINE`｜源 `E000019 ` → 重绘 `R000019`
28. `draw_arc`｜图层 `OUTLINE`｜源 `E000020 ` → 重绘 `R000020`
29. `draw_line`｜图层 `OUTLINE`｜源 `E000021 ` → 重绘 `R000021`
30. `draw_line`｜图层 `OUTLINE`｜源 `E000022 ` → 重绘 `R000022`
31. `draw_line`｜图层 `OUTLINE`｜源 `E000023 ` → 重绘 `R000023`
32. `draw_line`｜图层 `OUTLINE`｜源 `E000024 ` → 重绘 `R000024`
33. `draw_line`｜图层 `OUTLINE`｜源 `E000025 ` → 重绘 `R000025`
34. `draw_line`｜图层 `OUTLINE`｜源 `E000026 ` → 重绘 `R000026`
35. `draw_line`｜图层 `OUTLINE`｜源 `E000027 ` → 重绘 `R000027`
36. `draw_line`｜图层 `OUTLINE`｜源 `E000028 ` → 重绘 `R000028`
37. `draw_line`｜图层 `OUTLINE`｜源 `E000029 ` → 重绘 `R000029`
38. `draw_line`｜图层 `WALL1`｜源 `E000030 ` → 重绘 `R000030`
39. `draw_line`｜图层 `OUTLINE`｜源 `E000031 ` → 重绘 `R000031`
40. `draw_line`｜图层 `OUTLINE`｜源 `E000032 ` → 重绘 `R000032`
41. `draw_circle`｜图层 `WALL1`｜源 `E000033 ` → 重绘 `R000033`
42. `draw_line`｜图层 `DOTE`｜源 `E000034 ` → 重绘 `R000034`
43. `draw_line`｜图层 `WALL1`｜源 `E000035 ` → 重绘 `R000035`
44. `draw_line`｜图层 `WALL1`｜源 `E000036 ` → 重绘 `R000036`
45. `draw_line`｜图层 `WALL1`｜源 `E000037 ` → 重绘 `R000037`
46. `draw_line`｜图层 `WALL1`｜源 `E000038 ` → 重绘 `R000038`
47. `draw_line`｜图层 `WALL1`｜源 `E000039 ` → 重绘 `R000039`
48. `draw_line`｜图层 `WALL1`｜源 `E000040 ` → 重绘 `R000040`
49. `draw_arc`｜图层 `WALL1`｜源 `E000041 ` → 重绘 `R000041`
50. `draw_arc`｜图层 `WALL1`｜源 `E000042 ` → 重绘 `R000042`
51. `draw_line`｜图层 `WALL1`｜源 `E000043 ` → 重绘 `R000043`
52. `draw_line`｜图层 `WALL1`｜源 `E000044 ` → 重绘 `R000044`
53. `draw_line`｜图层 `WALL1`｜源 `E000045 ` → 重绘 `R000045`
54. `draw_line`｜图层 `WALL1`｜源 `E000046 ` → 重绘 `R000046`
55. `draw_line`｜图层 `WALL1`｜源 `E000047 ` → 重绘 `R000047`
56. `draw_line`｜图层 `WALL1`｜源 `E000048 ` → 重绘 `R000048`
57. `insert_block`｜图层 `WALL1`｜源 `E000051 ` → 重绘 `R000051`
58. `insert_block`｜图层 `WALL1`｜源 `E000052 ` → 重绘 `R000052`
59. `insert_block`｜图层 `WALL1`｜源 `E000053 ` → 重绘 `R000053`
60. `insert_block`｜图层 `WALL1`｜源 `E000054 ` → 重绘 `R000054`
61. `insert_block`｜图层 `WALL1`｜源 `E000055 ` → 重绘 `R000055`
62. `insert_block`｜图层 `WALL1`｜源 `E000056 ` → 重绘 `R000056`
63. `insert_block`｜图层 `WALL1`｜源 `E000057 ` → 重绘 `R000057`
64. `insert_block`｜图层 `WALL1`｜源 `E000058 ` → 重绘 `R000058`
65. `insert_block`｜图层 `WALL1`｜源 `E000059 ` → 重绘 `R000059`
66. `insert_block`｜图层 `WALL1`｜源 `E000060 ` → 重绘 `R000060`
67. `insert_block`｜图层 `WALL1`｜源 `E000061 ` → 重绘 `R000061`
68. `insert_block`｜图层 `WALL1`｜源 `E000062 ` → 重绘 `R000062`
69. `insert_block`｜图层 `WALL1`｜源 `E000063 ` → 重绘 `R000063`
70. `insert_block`｜图层 `WALL1`｜源 `E000064 ` → 重绘 `R000064`
71. `insert_block`｜图层 `WALL1`｜源 `E000070 ` → 重绘 `R000070`
72. `insert_block`｜图层 `WALL1`｜源 `E000071 ` → 重绘 `R000071`
73. `insert_block`｜图层 `WALL1`｜源 `E000072 ` → 重绘 `R000072`
74. `insert_block`｜图层 `WALL1`｜源 `E000073 ` → 重绘 `R000073`
75. `insert_block`｜图层 `WALL1`｜源 `E000074 ` → 重绘 `R000074`
76. `insert_block`｜图层 `WALL1`｜源 `E000075 ` → 重绘 `R000075`
77. `insert_block`｜图层 `WALL1`｜源 `E000080 ` → 重绘 `R000080`
78. `insert_block`｜图层 `WALL1`｜源 `E000081 ` → 重绘 `R000081`
79. `insert_block`｜图层 `WALL1`｜源 `E000082 ` → 重绘 `R000082`
80. `insert_block`｜图层 `WALL1`｜源 `E000084 ` → 重绘 `R000084`
81. `insert_block`｜图层 `WALL1`｜源 `E000085 ` → 重绘 `R000085`
82. `insert_block`｜图层 `WALL1`｜源 `E000086 ` → 重绘 `R000086`
83. `insert_block`｜图层 `WALL1`｜源 `E000087 ` → 重绘 `R000087`
84. `insert_block`｜图层 `WALL1`｜源 `E000088 ` → 重绘 `R000088`
85. `draw_line`｜图层 `DOTE`｜源 `E000089 ` → 重绘 `R000089`
86. `draw_line`｜图层 `OUTLINE`｜源 `E000090 ` → 重绘 `R000090`
87. `draw_line`｜图层 `OUTLINE`｜源 `E000091 ` → 重绘 `R000091`
88. `draw_line`｜图层 `WALL1`｜源 `E000092 ` → 重绘 `R000092`
89. `draw_line`｜图层 `OUTLINE`｜源 `E000093 ` → 重绘 `R000093`
90. `draw_line`｜图层 `OUTLINE`｜源 `E000094 ` → 重绘 `R000094`
91. `draw_line`｜图层 `OUTLINE`｜源 `E000095 ` → 重绘 `R000095`
92. `draw_line`｜图层 `OUTLINE`｜源 `E000096 ` → 重绘 `R000096`
93. `draw_line`｜图层 `OUTLINE`｜源 `E000097 ` → 重绘 `R000097`
94. `draw_line`｜图层 `OUTLINE`｜源 `E000098 ` → 重绘 `R000098`
95. `draw_line`｜图层 `OUTLINE`｜源 `E000099 ` → 重绘 `R000099`
96. `draw_line`｜图层 `OUTLINE`｜源 `E000100 ` → 重绘 `R000100`
97. `draw_line`｜图层 `OUTLINE`｜源 `E000101 ` → 重绘 `R000101`
98. `draw_line`｜图层 `WALL1`｜源 `E000102 ` → 重绘 `R000102`
99. `draw_line`｜图层 `WALL1`｜源 `E000104 ` → 重绘 `R000104`
100. `draw_line`｜图层 `WALL1`｜源 `E000105 ` → 重绘 `R000105`
101. `draw_circle`｜图层 `WALL1`｜源 `E000106 ` → 重绘 `R000106`
102. `draw_line`｜图层 `DOTE`｜源 `E000107 ` → 重绘 `R000107`
103. `draw_line`｜图层 `DOTE`｜源 `E000108 ` → 重绘 `R000108`
104. `draw_arc`｜图层 `OUTLINE`｜源 `E000109 ` → 重绘 `R000109`
105. `draw_arc`｜图层 `OUTLINE`｜源 `E000110 ` → 重绘 `R000110`
106. `draw_line`｜图层 `WALL1`｜源 `E000111 ` → 重绘 `R000111`
107. `draw_arc`｜图层 `OUTLINE`｜源 `E000112 ` → 重绘 `R000112`
108. `draw_line`｜图层 `OUTLINE`｜源 `E000113 ` → 重绘 `R000113`
109. `draw_line`｜图层 `OUTLINE`｜源 `E000114 ` → 重绘 `R000114`
110. `draw_line`｜图层 `OUTLINE`｜源 `E000115 ` → 重绘 `R000115`
111. `draw_line`｜图层 `OUTLINE`｜源 `E000116 ` → 重绘 `R000116`
112. `draw_line`｜图层 `WALL1`｜源 `E000117 ` → 重绘 `R000117`
113. `draw_line`｜图层 `WALL1`｜源 `E000118 ` → 重绘 `R000118`
114. `draw_line`｜图层 `WALL1`｜源 `E000120 ` → 重绘 `R000120`
115. `draw_arc`｜图层 `WALL1`｜源 `E000121 ` → 重绘 `R000121`
116. `draw_line`｜图层 `WALL1`｜源 `E000122 ` → 重绘 `R000122`
117. `draw_line`｜图层 `WALL1`｜源 `E000123 ` → 重绘 `R000123`
118. `draw_line`｜图层 `WALL1`｜源 `E000124 ` → 重绘 `R000124`
119. `draw_line`｜图层 `DOTE`｜源 `E000125 ` → 重绘 `R000125`
120. `draw_arc`｜图层 `OUTLINE`｜源 `E000126 ` → 重绘 `R000126`
121. `draw_arc`｜图层 `OUTLINE`｜源 `E000127 ` → 重绘 `R000127`
122. `draw_line`｜图层 `WALL1`｜源 `E000128 ` → 重绘 `R000128`
123. `draw_line`｜图层 `OUTLINE`｜源 `E000129 ` → 重绘 `R000129`
124. `draw_arc`｜图层 `OUTLINE`｜源 `E000130 ` → 重绘 `R000130`
125. `draw_line`｜图层 `OUTLINE`｜源 `E000131 ` → 重绘 `R000131`
126. `draw_line`｜图层 `OUTLINE`｜源 `E000132 ` → 重绘 `R000132`
127. `draw_line`｜图层 `WALL1`｜源 `E000133 ` → 重绘 `R000133`
128. `draw_line`｜图层 `WALL1`｜源 `E000134 ` → 重绘 `R000134`
129. `draw_line`｜图层 `OUTLINE`｜源 `E000135 ` → 重绘 `R000135`
130. `draw_arc`｜图层 `WALL1`｜源 `E000136 ` → 重绘 `R000136`
131. `draw_line`｜图层 `WALL1`｜源 `E000137 ` → 重绘 `R000137`
132. `draw_line`｜图层 `WALL1`｜源 `E000138 ` → 重绘 `R000138`
133. `add_text`｜图层 `PUB_TEXT`｜源 `E000049 ` → 重绘 `R000049`
134. `add_text`｜图层 `PUB_TEXT`｜源 `E000050 ` → 重绘 `R000050`
135. `add_text`｜图层 `PUB_TEXT`｜源 `E000065 ` → 重绘 `R000065`
136. `add_text`｜图层 `PUB_TEXT`｜源 `E000066 ` → 重绘 `R000066`
137. `add_text`｜图层 `PUB_TEXT`｜源 `E000067 ` → 重绘 `R000067`
138. `add_text`｜图层 `PUB_TEXT`｜源 `E000068 ` → 重绘 `R000068`
139. `add_text`｜图层 `PUB_TEXT`｜源 `E000069 ` → 重绘 `R000069`
140. `add_text`｜图层 `PUB_TEXT`｜源 `E000076 ` → 重绘 `R000076`
141. `add_text`｜图层 `PUB_TEXT`｜源 `E000077 ` → 重绘 `R000077`
142. `add_text`｜图层 `PUB_TEXT`｜源 `E000078 ` → 重绘 `R000078`
143. `add_text`｜图层 `PUB_TEXT`｜源 `E000079 ` → 重绘 `R000079`
144. `add_text`｜图层 `PUB_TEXT`｜源 `E000083 ` → 重绘 `R000083`
145. `add_text`｜图层 `PUB_TEXT`｜源 `E000103 ` → 重绘 `R000103`
146. `add_text`｜图层 `PUB_TEXT`｜源 `E000119 ` → 重绘 `R000119`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
