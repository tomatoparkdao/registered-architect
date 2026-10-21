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
    "LINE": 1211,
    "ARC": 16,
    "CIRCLE": 10,
    "SPLINE": 2,
    "HATCH": 8,
    "INSERT": 52,
    "POLYLINE": 22,
    "SOLID": 25,
    "LWPOLYLINE": 6,
    "TEXT": 58
  },
  "geometry_checksum": 793250103296.0,
  "bounds": [
    [
      -227681.05,
      -10464.2
    ],
    [
      67132.39,
      106598.41
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
