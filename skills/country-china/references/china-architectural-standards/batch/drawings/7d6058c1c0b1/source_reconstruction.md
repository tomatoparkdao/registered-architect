# 源图重绘配方

- 源 DWG：`图例.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[354565.91, 283854.38], [369355.88, 287986.88]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `WINDOW`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `WATER`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `TEXT`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `XU`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `GLASS`｜源 `- ` → 重绘 `-`
7. `create_layer`｜图层 `SG`｜源 `- ` → 重绘 `-`
8. `create_layer`｜图层 `KT`｜源 `- ` → 重绘 `-`
9. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
10. `draw_polyline`｜图层 `WINDOW`｜源 `E000001 ` → 重绘 `R000001`
11. `draw_polyline`｜图层 `WINDOW`｜源 `E000002 ` → 重绘 `R000002`
12. `draw_line`｜图层 `TEXT`｜源 `E000003 ` → 重绘 `R000003`
13. `draw_line`｜图层 `TEXT`｜源 `E000004 ` → 重绘 `R000004`
14. `draw_line`｜图层 `TEXT`｜源 `E000005 ` → 重绘 `R000005`
15. `draw_line`｜图层 `TEXT`｜源 `E000006 ` → 重绘 `R000006`
16. `draw_line`｜图层 `TEXT`｜源 `E000007 ` → 重绘 `R000007`
17. `draw_line`｜图层 `TEXT`｜源 `E000008 ` → 重绘 `R000008`
18. `draw_circle`｜图层 `WATER`｜源 `E000009 ` → 重绘 `R000009`
19. `hatch`｜图层 `WATER`｜源 `E000010 ` → 重绘 `R000010`
20. `draw_line`｜图层 `WATER`｜源 `E000011 ` → 重绘 `R000011`
21. `draw_polyline`｜图层 `WINDOW`｜源 `E000012 ` → 重绘 `R000012`
22. `draw_polyline`｜图层 `WINDOW`｜源 `E000013 ` → 重绘 `R000013`
23. `add_leader`｜图层 `KT`｜源 `E000015 ` → 重绘 `R000015`
24. `draw_polyline`｜图层 `XU`｜源 `E000016 ` → 重绘 `R000016`
25. `draw_line`｜图层 `TEXT`｜源 `E000018 ` → 重绘 `R000018`
26. `draw_line`｜图层 `TEXT`｜源 `E000019 ` → 重绘 `R000019`
27. `draw_line`｜图层 `TEXT`｜源 `E000020 ` → 重绘 `R000020`
28. `draw_line`｜图层 `TEXT`｜源 `E000025 ` → 重绘 `R000025`
29. `draw_line`｜图层 `TEXT`｜源 `E000030 ` → 重绘 `R000030`
30. `draw_line`｜图层 `TEXT`｜源 `E000033 ` → 重绘 `R000033`
31. `draw_line`｜图层 `TEXT`｜源 `E000034 ` → 重绘 `R000034`
32. `draw_line`｜图层 `TEXT`｜源 `E000035 ` → 重绘 `R000035`
33. `draw_line`｜图层 `TEXT`｜源 `E000036 ` → 重绘 `R000036`
34. `draw_line`｜图层 `TEXT`｜源 `E000037 ` → 重绘 `R000037`
35. `draw_line`｜图层 `TEXT`｜源 `E000038 ` → 重绘 `R000038`
36. `draw_polyline`｜图层 `WINDOW`｜源 `E000039 ` → 重绘 `R000039`
37. `draw_polyline`｜图层 `WINDOW`｜源 `E000040 ` → 重绘 `R000040`
38. `draw_line`｜图层 `XU`｜源 `E000041 ` → 重绘 `R000041`
39. `draw_line`｜图层 `XU`｜源 `E000042 ` → 重绘 `R000042`
40. `draw_line`｜图层 `XU`｜源 `E000043 ` → 重绘 `R000043`
41. `draw_line`｜图层 `XU`｜源 `E000044 ` → 重绘 `R000044`
42. `draw_polyline`｜图层 `SG`｜源 `E000045 ` → 重绘 `R000045`
43. `draw_line`｜图层 `XU`｜源 `E000046 ` → 重绘 `R000046`
44. `draw_line`｜图层 `XU`｜源 `E000047 ` → 重绘 `R000047`
45. `draw_polyline`｜图层 `XU`｜源 `E000048 ` → 重绘 `R000048`
46. `draw_line`｜图层 `SG`｜源 `E000049 ` → 重绘 `R000049`
47. `draw_line`｜图层 `SG`｜源 `E000050 ` → 重绘 `R000050`
48. `draw_line`｜图层 `SG`｜源 `E000051 ` → 重绘 `R000051`
49. `draw_polyline`｜图层 `SG`｜源 `E000052 ` → 重绘 `R000052`
50. `draw_circle`｜图层 `SG`｜源 `E000053 ` → 重绘 `R000053`
51. `draw_line`｜图层 `SG`｜源 `E000054 ` → 重绘 `R000054`
52. `draw_line`｜图层 `SG`｜源 `E000055 ` → 重绘 `R000055`
53. `draw_line`｜图层 `TEXT`｜源 `E000057 ` → 重绘 `R000057`
54. `draw_line`｜图层 `TEXT`｜源 `E000058 ` → 重绘 `R000058`
55. `draw_line`｜图层 `TEXT`｜源 `E000059 ` → 重绘 `R000059`
56. `draw_line`｜图层 `TEXT`｜源 `E000065 ` → 重绘 `R000065`
57. `add_mtext`｜图层 `KT`｜源 `E000014 ` → 重绘 `R000014`
58. `add_text`｜图层 `GLASS`｜源 `E000017 ` → 重绘 `R000017`
59. `add_text`｜图层 `TEXT`｜源 `E000021 ` → 重绘 `R000021`
60. `add_text`｜图层 `TEXT`｜源 `E000022 ` → 重绘 `R000022`
61. `add_text`｜图层 `TEXT`｜源 `E000023 ` → 重绘 `R000023`
62. `add_text`｜图层 `GLASS`｜源 `E000024 ` → 重绘 `R000024`
63. `add_text`｜图层 `TEXT`｜源 `E000026 ` → 重绘 `R000026`
64. `add_text`｜图层 `TEXT`｜源 `E000027 ` → 重绘 `R000027`
65. `add_text`｜图层 `TEXT`｜源 `E000028 ` → 重绘 `R000028`
66. `add_text`｜图层 `TEXT`｜源 `E000029 ` → 重绘 `R000029`
67. `add_text`｜图层 `TEXT`｜源 `E000031 ` → 重绘 `R000031`
68. `add_text`｜图层 `TEXT`｜源 `E000032 ` → 重绘 `R000032`
69. `add_text`｜图层 `GLASS`｜源 `E000056 ` → 重绘 `R000056`
70. `add_text`｜图层 `TEXT`｜源 `E000060 ` → 重绘 `R000060`
71. `add_text`｜图层 `TEXT`｜源 `E000061 ` → 重绘 `R000061`
72. `add_text`｜图层 `TEXT`｜源 `E000062 ` → 重绘 `R000062`
73. `add_text`｜图层 `TEXT`｜源 `E000063 ` → 重绘 `R000063`
74. `add_text`｜图层 `GLASS`｜源 `E000064 ` → 重绘 `R000064`
