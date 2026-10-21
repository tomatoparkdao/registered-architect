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
    "LINE": 2530,
    "ARC": 284,
    "HATCH": 99,
    "LWPOLYLINE": 80,
    "CIRCLE": 137,
    "MTEXT": 11,
    "TEXT": 1,
    "DIMENSION": 42
  },
  "geometry_checksum": 128761380864.0,
  "bounds": [
    [
      0.0,
      -366.73
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
