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
    "CIRCLE": 9,
    "LWPOLYLINE": 100,
    "HATCH": 15,
    "LINE": 362,
    "ARC": 128,
    "LEADER": 29,
    "TEXT": 43,
    "DIMENSION": 56
  },
  "geometry_checksum": 13413074944.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      3385.67,
      4587.94
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
