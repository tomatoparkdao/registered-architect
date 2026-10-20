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
    "LEADER": 14,
    "POLYLINE": 215,
    "ARC": 140,
    "CIRCLE": 10,
    "LWPOLYLINE": 159,
    "ELLIPSE": 6,
    "LINE": 264,
    "HATCH": 4,
    "SPLINE": 5,
    "TEXT": 14
  },
  "geometry_checksum": 3370266394624.0,
  "bounds": [
    [
      985.73,
      311.67
    ],
    [
      35871.33,
      62607.72
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
