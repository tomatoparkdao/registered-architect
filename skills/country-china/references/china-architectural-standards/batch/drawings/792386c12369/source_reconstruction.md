# 源图重绘配方

- 源 DWG：`门框角钢加门.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[82595.61, 18237.7], [82882.26, 20499.56]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `PUB_TITLE`｜源 `- ` → 重绘 `-`
3. `create_layer`｜图层 `角钢`｜源 `- ` → 重绘 `-`
4. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
5. `insert_block`｜图层 `角钢`｜源 `E000001 ` → 重绘 `R000001`
6. `draw_polyline`｜图层 `角钢`｜源 `E000002 ` → 重绘 `R000002`
