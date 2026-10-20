# 解析报告

```json
{
  "result": "geometry_extracted",
  "gpu_execution": {
    "device": "NVIDIA GeForce RTX 4070",
    "cuda_available": true,
    "operations": [
      "model-space coordinate tensor construction",
      "CUDA bounds reduction",
      "CUDA geometry checksum",
      "CUDA nearest-geometry association for text and dimensions"
    ]
  },
  "entity_counts": {
    "LINE": 1322,
    "ARC": 27,
    "LWPOLYLINE": 104,
    "CIRCLE": 28,
    "HATCH": 3,
    "TEXT": 127,
    "DIMENSION": 134
  },
  "geometry_checksum": 576270827520.0,
  "bounds": [
    [
      1064.99,
      3561.76
    ],
    [
      37976.06,
      29485.3
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
