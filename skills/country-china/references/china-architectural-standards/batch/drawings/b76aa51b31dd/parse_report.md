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
    "LINE": 260,
    "LWPOLYLINE": 98,
    "HATCH": 24,
    "LEADER": 35,
    "CIRCLE": 10,
    "ARC": 24,
    "TEXT": 52,
    "DIMENSION": 34
  },
  "geometry_checksum": 59514032128.0,
  "bounds": [
    [
      -754.14,
      0.0
    ],
    [
      12529.8,
      20255.47
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
