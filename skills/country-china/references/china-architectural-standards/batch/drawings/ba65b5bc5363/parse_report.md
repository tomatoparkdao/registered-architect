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
    "LINE": 1439,
    "LWPOLYLINE": 371,
    "ARC": 569,
    "SPLINE": 48,
    "LEADER": 5,
    "CIRCLE": 28,
    "HATCH": 15,
    "ELLIPSE": 408,
    "TEXT": 10,
    "DIMENSION": 66
  },
  "geometry_checksum": 206431551488.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      5202.21,
      5339.82
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
