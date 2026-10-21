# 重绘验证报告

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。


## 计数口径与结论

- 先前的 `27` 是含 6 个 HATCH 的几何记录数：`21` 个非填充几何 + `6` 个 HATCH；不是总模型空间实体数。
- 总模型空间实体为 `27` 几何记录 + `7` 个 TEXT/MTEXT + `5` 个 DIMENSION = `39`。源图与重绘图在该口径下均为 39。
- 本样本没有 LEADER 或模型空间 INSERT。源图的 21 个命名块没有被 INSERT 引用，故独立 Recipe 不复制无效库块；重绘文件唯一命名块是 CAD 默认尺寸样式支持块，非模型空间实体。5 个匿名 `*D` 块由对应 DIMENSION 的 CAD 渲染步骤生成。
- `entity_handle_map.json` 为 39 个源模型空间实体逐项给出源句柄与重绘句柄；没有无来源的模型空间几何。

```json
{
  "status": "reconstructed_by_independently_executing_cad_recipe",
  "reconstructed_dxf": "reconstruction/CN-DWG-5DA4FD9A038E-reconstructed.dxf",
  "entity_handle_map": "reconstruction/entity_handle_map.json",
  "source_geometry_checksum": -4477662.0,
  "model_space_type_counts": {
    "source": {
      "LINE": 5,
      "CIRCLE": 1
    },
    "reconstructed": {
      "LINE": 5,
      "CIRCLE": 1
    }
  },
  "category_counts": {
    "geometry_excluding_hatch": {
      "source": 6,
      "reconstructed": 6
    },
    "geometry_including_hatch": {
      "source": 6,
      "reconstructed": 6
    },
    "TEXT_MTEXT": {
      "source": 0,
      "reconstructed": 0
    },
    "DIMENSION": {
      "source": 0,
      "reconstructed": 0
    },
    "LEADER": {
      "source": 0,
      "reconstructed": 0
    },
    "HATCH": {
      "source": 0,
      "reconstructed": 0
    },
    "INSERT_model_space": {
      "source": 0,
      "reconstructed": 0
    },
    "model_space_total": {
      "source": 6,
      "reconstructed": 6
    }
  },
  "block_summary": {
    "named_block_definitions": {
      "source": 21,
      "reconstructed": 0,
      "explanation": "源图 21 个命名块均未被模型空间 INSERT 引用，因此独立 Recipe 不复制未使用库块。重绘文件的 1 个命名块由 CAD 默认尺寸样式支持生成，非模型空间几何。"
    },
    "anonymous_dimension_blocks": {
      "source": 0,
      "reconstructed": 0,
      "explanation": "每个 DIMENSION 的图形由 CAD 尺寸渲染器在匿名 *D 块中生成；该类块不是额外模型空间几何。"
    }
  },
  "handle_mapping": {
    "mapped_source_modelspace_entities": 6,
    "expected_source_modelspace_entities": 6,
    "complete": true,
    "system_generated_modelspace_entities": 0,
    "system_generated_non_modelspace_entities": "匿名 *D 尺寸块内图元；均由对应 DIMENSION 重绘步骤生成。"
  },
  "gpu_device": "NVIDIA GeForce RTX 4070",
  "source_bounds": [
    [
      109145.39,
      -134698.52
    ],
    [
      109347.34,
      -133774.36
    ]
  ],
  "reconstructed_bounds": [
    [
      109145.39,
      -134698.52
    ],
    [
      109347.34,
      -133774.36
    ]
  ],
  "max_bound_delta": 0.0,
  "bounds_match_within_tolerance": true,
  "comparison": "重绘 DXF 由 cad_recipe.json 独立执行生成；模型空间每类实体数量、边界和逐实体句柄映射均已核验。DIMENSION 关联为 GPU 近邻候选，仍明确标记为待人工复核。"
}
```

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
