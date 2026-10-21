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
    "HATCH": 5,
    "LINE": 627,
    "LEADER": 12,
    "INSERT": 2,
    "CIRCLE": 6,
    "ARC": 28,
    "SPLINE": 24,
    "TEXT": 6,
    "MTEXT": 9,
    "DIMENSION": 8
  },
  "geometry_checksum": 565639249920.0,
  "bounds": [
    [
      286971.62,
      -2053.6
    ],
    [
      290219.75,
      -708.82
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
