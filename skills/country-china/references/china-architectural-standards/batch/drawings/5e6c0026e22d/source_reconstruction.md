# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`DY-挑檐详图C.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[17241.18, 10177.95], [17809.22, 10800.0]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `WALL`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `WINDOW`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `PUB_DIM`｜源 `- ` → 重绘 `-`
5. `create_layer`｜图层 `DEFPOINTS`｜源 `- ` → 重绘 `-`
6. `create_layer`｜图层 `S_SURFACE`｜源 `- ` → 重绘 `-`
7. `create_layer`｜图层 `PUB_TEXT`｜源 `- ` → 重绘 `-`
8. `create_layer`｜图层 `PUB_HATCH`｜源 `- ` → 重绘 `-`
9. `create_layer`｜图层 `DOTE`｜源 `- ` → 重绘 `-`
10. `create_layer`｜图层 `SURFACE`｜源 `- ` → 重绘 `-`
11. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000003 ` → 重绘 `R000003`
12. `draw_polyline`｜图层 `PUB_TEXT`｜源 `E000004 ` → 重绘 `R000004`
13. `insert_block`｜图层 `0`｜源 `E000005 ` → 重绘 `R000005`
14. `add_text`｜图层 `PUB_TEXT`｜源 `E000001 ` → 重绘 `R000001`
15. `add_text`｜图层 `PUB_TEXT`｜源 `E000002 ` → 重绘 `R000002`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
