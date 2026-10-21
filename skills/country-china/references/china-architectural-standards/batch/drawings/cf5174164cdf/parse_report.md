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
    "CIRCLE": 74,
    "LINE": 5872,
    "ARC": 448,
    "HATCH": 204,
    "LWPOLYLINE": 485,
    "LEADER": 27,
    "INSERT": 149,
    "SOLID": 8,
    "TEXT": 158,
    "MTEXT": 1
  },
  "geometry_checksum": 34791309180928.0,
  "bounds": [
    [
      105430.38,
      -29787.13
    ],
    [
      136421.05,
      88998.3
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
