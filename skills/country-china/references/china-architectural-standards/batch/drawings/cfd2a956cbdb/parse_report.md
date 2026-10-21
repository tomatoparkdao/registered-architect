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
    "LINE": 955,
    "HATCH": 54,
    "CIRCLE": 38,
    "ARC": 137,
    "LWPOLYLINE": 14,
    "SOLID": 3,
    "MTEXT": 29,
    "TEXT": 1,
    "DIMENSION": 21
  },
  "geometry_checksum": 62283878400.0,
  "bounds": [
    [
      0.0,
      -188.95
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
