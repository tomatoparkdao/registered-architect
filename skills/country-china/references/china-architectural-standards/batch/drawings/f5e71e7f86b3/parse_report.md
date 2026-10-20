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
    "LEADER": 29,
    "LINE": 434,
    "HATCH": 38,
    "LWPOLYLINE": 84,
    "ARC": 107,
    "CIRCLE": 4,
    "SPLINE": 1,
    "ELLIPSE": 1,
    "INSERT": 1,
    "TEXT": 55,
    "DIMENSION": 30
  },
  "geometry_checksum": 21216800768.0,
  "bounds": [
    [
      101.19,
      138.73
    ],
    [
      5415.86,
      6586.88
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
