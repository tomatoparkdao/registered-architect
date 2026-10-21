# 源图重绘配方

- 源 DWG：`梯扶手.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[2853.86, -816.97], [3306.37, -377.13]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `DEFPOINTS`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `PUB_TEXT`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `PUB_DIM`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `S_WALL`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `S_SURFACE`｜源 `- ` → 重绘 `-`
7. `draw_line`｜图层 `S_WALL`｜源 `E000001 ` → 重绘 `R000001`
8. `draw_line`｜图层 `S_WALL`｜源 `E000002 ` → 重绘 `R000002`
9. `draw_polyline`｜图层 `S_WALL`｜源 `E000003 ` → 重绘 `R000003`
10. `hatch`｜图层 `S_SURFACE`｜源 `E000004 ` → 重绘 `R000004`
11. `draw_polyline`｜图层 `0`｜源 `E000006 ` → 重绘 `R000006`
12. `draw_polyline`｜图层 `0`｜源 `E000007 ` → 重绘 `R000007`
13. `draw_circle`｜图层 `PUB_TEXT`｜源 `E000008 ` → 重绘 `R000008`
14. `draw_line`｜图层 `S_SURFACE`｜源 `E000010 ` → 重绘 `R000010`
15. `draw_line`｜图层 `S_SURFACE`｜源 `E000011 ` → 重绘 `R000011`
16. `draw_line`｜图层 `S_SURFACE`｜源 `E000012 ` → 重绘 `R000012`
17. `draw_line`｜图层 `S_SURFACE`｜源 `E000013 ` → 重绘 `R000013`
18. `draw_circle`｜图层 `S_SURFACE`｜源 `E000014 ` → 重绘 `R000014`
19. `draw_line`｜图层 `S_SURFACE`｜源 `E000015 ` → 重绘 `R000015`
20. `draw_line`｜图层 `S_SURFACE`｜源 `E000016 ` → 重绘 `R000016`
21. `draw_arc`｜图层 `S_SURFACE`｜源 `E000017 ` → 重绘 `R000017`
22. `draw_arc`｜图层 `S_SURFACE`｜源 `E000018 ` → 重绘 `R000018`
23. `draw_line`｜图层 `S_SURFACE`｜源 `E000019 ` → 重绘 `R000019`
24. `draw_line`｜图层 `S_SURFACE`｜源 `E000020 ` → 重绘 `R000020`
25. `draw_line`｜图层 `S_SURFACE`｜源 `E000021 ` → 重绘 `R000021`
26. `draw_line`｜图层 `S_SURFACE`｜源 `E000022 ` → 重绘 `R000022`
27. `draw_line`｜图层 `S_SURFACE`｜源 `E000023 ` → 重绘 `R000023`
28. `draw_line`｜图层 `S_SURFACE`｜源 `E000024 ` → 重绘 `R000024`
29. `draw_circle`｜图层 `S_SURFACE`｜源 `E000025 ` → 重绘 `R000025`
30. `draw_line`｜图层 `S_SURFACE`｜源 `E000026 ` → 重绘 `R000026`
31. `draw_line`｜图层 `S_SURFACE`｜源 `E000027 ` → 重绘 `R000027`
32. `insert_block`｜图层 `PUB_DIM`｜源 `E000029 ` → 重绘 `R000029`
33. `draw_line`｜图层 `PUB_DIM`｜源 `E000030 ` → 重绘 `R000030`
34. `draw_line`｜图层 `S_WALL`｜源 `E000034 ` → 重绘 `R000034`
35. `draw_line`｜图层 `S_WALL`｜源 `E000035 ` → 重绘 `R000035`
36. `draw_line`｜图层 `S_WALL`｜源 `E000036 ` → 重绘 `R000036`
37. `draw_line`｜图层 `S_WALL`｜源 `E000037 ` → 重绘 `R000037`
38. `draw_line`｜图层 `S_WALL`｜源 `E000038 ` → 重绘 `R000038`
39. `draw_line`｜图层 `S_WALL`｜源 `E000039 ` → 重绘 `R000039`
40. `draw_line`｜图层 `S_WALL`｜源 `E000040 ` → 重绘 `R000040`
41. `draw_line`｜图层 `S_WALL`｜源 `E000041 ` → 重绘 `R000041`
42. `draw_line`｜图层 `S_WALL`｜源 `E000042 ` → 重绘 `R000042`
43. `hatch`｜图层 `S_SURFACE`｜源 `E000043 ` → 重绘 `R000043`
44. `hatch`｜图层 `S_SURFACE`｜源 `E000044 ` → 重绘 `R000044`
45. `draw_line`｜图层 `S_SURFACE`｜源 `E000052 ` → 重绘 `R000052`
46. `draw_line`｜图层 `S_SURFACE`｜源 `E000053 ` → 重绘 `R000053`
47. `draw_line`｜图层 `S_SURFACE`｜源 `E000054 ` → 重绘 `R000054`
48. `draw_line`｜图层 `S_SURFACE`｜源 `E000055 ` → 重绘 `R000055`
49. `draw_line`｜图层 `S_SURFACE`｜源 `E000056 ` → 重绘 `R000056`
50. `draw_line`｜图层 `S_SURFACE`｜源 `E000057 ` → 重绘 `R000057`
51. `draw_line`｜图层 `S_SURFACE`｜源 `E000058 ` → 重绘 `R000058`
52. `draw_line`｜图层 `S_SURFACE`｜源 `E000059 ` → 重绘 `R000059`
53. `draw_line`｜图层 `S_SURFACE`｜源 `E000060 ` → 重绘 `R000060`
54. `draw_line`｜图层 `S_SURFACE`｜源 `E000061 ` → 重绘 `R000061`
55. `draw_line`｜图层 `S_SURFACE`｜源 `E000062 ` → 重绘 `R000062`
56. `draw_line`｜图层 `S_SURFACE`｜源 `E000063 ` → 重绘 `R000063`
57. `draw_line`｜图层 `S_SURFACE`｜源 `E000064 ` → 重绘 `R000064`
58. `add_text`｜图层 `PUB_TEXT`｜源 `E000005 ` → 重绘 `R000005`
59. `add_text`｜图层 `PUB_TEXT`｜源 `E000009 ` → 重绘 `R000009`
60. `add_text`｜图层 `PUB_DIM`｜源 `E000028 ` → 重绘 `R000028`
61. `add_text`｜图层 `PUB_TEXT`｜源 `E000045 ` → 重绘 `R000045`
62. `add_text`｜图层 `PUB_TEXT`｜源 `E000047 ` → 重绘 `R000047`
63. `add_text`｜图层 `PUB_TEXT`｜源 `E000048 ` → 重绘 `R000048`
64. `add_text`｜图层 `PUB_TEXT`｜源 `E000049 ` → 重绘 `R000049`
65. `add_text`｜图层 `PUB_TEXT`｜源 `E000050 ` → 重绘 `R000050`
66. `add_text`｜图层 `PUB_TEXT`｜源 `E000051 ` → 重绘 `R000051`
67. `add_text`｜图层 `PUB_TEXT`｜源 `E000065 ` → 重绘 `R000065`
68. `add_text`｜图层 `PUB_TEXT`｜源 `E000066 ` → 重绘 `R000066`
69. `add_text`｜图层 `PUB_TEXT`｜源 `E000067 ` → 重绘 `R000067`
70. `add_dimension`｜图层 `PUB_DIM`｜源 `E000031 ` → 重绘 `R000031`
71. `add_dimension`｜图层 `PUB_DIM`｜源 `E000032 ` → 重绘 `R000032`
72. `add_dimension`｜图层 `PUB_DIM`｜源 `E000033 ` → 重绘 `R000033`
73. `add_dimension`｜图层 `PUB_DIM`｜源 `E000046 ` → 重绘 `R000046`
