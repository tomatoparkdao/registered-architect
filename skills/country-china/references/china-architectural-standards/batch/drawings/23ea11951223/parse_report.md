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
    "LEADER": 30,
    "LINE": 6499,
    "HATCH": 9,
    "LWPOLYLINE": 93,
    "INSERT": 6,
    "CIRCLE": 16,
    "ARC": 43,
    "ELLIPSE": 8,
    "SPLINE": 8,
    "TEXT": 41,
    "DIMENSION": 36
  },
  "geometry_checksum": 1544196980736.0,
  "bounds": [
    [
      -206545.58,
      -396.55
    ],
    [
      43042.24,
      7021.52
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
