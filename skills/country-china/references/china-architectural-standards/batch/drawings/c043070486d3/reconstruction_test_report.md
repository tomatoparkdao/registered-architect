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
  "reconstructed_dxf": "reconstruction/CN-DWG-C043070486D3-reconstructed.dxf",
  "entity_handle_map": "reconstruction/entity_handle_map.json",
  "source_geometry_checksum": 7874.68,
  "model_space_type_counts": {
    "source": {
      "LWPOLYLINE": 1,
      "LINE": 6
    },
    "reconstructed": {
      "LWPOLYLINE": 1,
      "LINE": 6
    }
  },
  "category_counts": {
    "geometry_excluding_hatch": {
      "source": 7,
      "reconstructed": 7
    },
    "geometry_including_hatch": {
      "source": 7,
      "reconstructed": 7
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
      "source": 7,
      "reconstructed": 7
    }
  },
  "block_summary": {
    "named_block_definitions": {
      "source": 20,
      "reconstructed": 20,
      "explanation": "\u6e90\u56fe 21 \u4e2a\u547d\u540d\u5757\u5747\u672a\u88ab\u6a21\u578b\u7a7a\u95f4 INSERT \u5f15\u7528\uff0c\u56e0\u6b64\u72ec\u7acb Recipe \u4e0d\u590d\u5236\u672a\u4f7f\u7528\u5e93\u5757\u3002\u91cd\u7ed8\u6587\u4ef6\u7684 1 \u4e2a\u547d\u540d\u5757\u7531 CAD \u9ed8\u8ba4\u5c3a\u5bf8\u6837\u5f0f\u652f\u6301\u751f\u6210\uff0c\u975e\u6a21\u578b\u7a7a\u95f4\u51e0\u4f55\u3002"
    },
    "anonymous_dimension_blocks": {
      "source": 0,
      "reconstructed": 0,
      "explanation": "\u6bcf\u4e2a DIMENSION \u7684\u56fe\u5f62\u7531 CAD \u5c3a\u5bf8\u6e32\u67d3\u5668\u5728\u533f\u540d *D \u5757\u4e2d\u751f\u6210\uff1b\u8be5\u7c7b\u5757\u4e0d\u662f\u989d\u5916\u6a21\u578b\u7a7a\u95f4\u51e0\u4f55\u3002"
    }
  },
  "handle_mapping": {
    "mapped_source_modelspace_entities": 7,
    "expected_source_modelspace_entities": 7,
    "complete": true,
    "system_generated_modelspace_entities": 0,
    "system_generated_non_modelspace_entities": "\u533f\u540d *D \u5c3a\u5bf8\u5757\u5185\u56fe\u5143\uff1b\u5747\u7531\u5bf9\u5e94 DIMENSION \u91cd\u7ed8\u6b65\u9aa4\u751f\u6210\u3002"
  },
  "gpu_device": "NVIDIA GeForce RTX 4070",
  "source_bounds": [
    [
      9.48,
      11.93
    ],
    [
      39.48,
      18.67
    ]
  ],
  "reconstructed_bounds": [
    [
      9.48,
      11.93
    ],
    [
      39.48,
      18.67
    ]
  ],
  "max_bound_delta": 0.0,
  "bounds_match_within_tolerance": true,
  "comparison": "\u91cd\u7ed8 DXF \u7531 cad_recipe.json \u72ec\u7acb\u6267\u884c\u751f\u6210\uff1b\u6a21\u578b\u7a7a\u95f4\u6bcf\u7c7b\u5b9e\u4f53\u6570\u91cf\u3001\u8fb9\u754c\u548c\u9010\u5b9e\u4f53\u53e5\u67c4\u6620\u5c04\u5747\u5df2\u6838\u9a8c\u3002DIMENSION \u5173\u8054\u4e3a GPU \u8fd1\u90bb\u5019\u9009\uff0c\u4ecd\u660e\u786e\u6807\u8bb0\u4e3a\u5f85\u4eba\u5de5\u590d\u6838\u3002"
}
```

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
