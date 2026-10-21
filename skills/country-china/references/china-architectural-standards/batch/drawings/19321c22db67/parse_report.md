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
    "ARC": 14,
    "LINE": 551,
    "LWPOLYLINE": 170,
    "CIRCLE": 7,
    "SPLINE": 1,
    "INSERT": 45,
    "HATCH": 39,
    "TEXT": 125,
    "DIMENSION": 124
  },
  "geometry_checksum": 459634442240.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      25594.0,
      38169.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
