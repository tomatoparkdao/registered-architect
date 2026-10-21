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
    "INSERT": 9,
    "LINE": 633,
    "ARC": 48,
    "CIRCLE": 23,
    "LWPOLYLINE": 28,
    "SOLID": 2,
    "HATCH": 17,
    "MTEXT": 19,
    "TEXT": 1,
    "DIMENSION": 23
  },
  "geometry_checksum": 6795108352.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      724029.19,
      309406.72
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
