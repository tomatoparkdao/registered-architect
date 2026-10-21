# 源图重绘配方

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


- 源 DWG：`新建的有架线的窄轨电气铁路.dwg`
- 临时 DXF：仅用于解析，不进入 Skill。
- 坐标系：模型空间；单位：`unknown ($INSUNITS=0)`；边界：`[[9.28, 16.46], [39.28, 19.57]]`。
- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。
- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。

## CAD 绘图步骤

1. `create_layer`｜图层 `0`｜源 `- ` → 重绘 `-`
2. `create_layer`｜图层 `Defpoints`｜源 `- ` → 重绘 `-`
3. `draw_polyline`｜图层 `0`｜源 `E000001 ` → 重绘 `R000001`
4. `draw_line`｜图层 `0`｜源 `E000002 ` → 重绘 `R000002`
5. `draw_line`｜图层 `0`｜源 `E000003 ` → 重绘 `R000003`
6. `insert_block`｜图层 `0`｜源 `E000005 ` → 重绘 `R000005`
7. `add_text`｜图层 `0`｜源 `E000004 ` → 重绘 `R000004`

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
