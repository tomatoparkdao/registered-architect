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
    "LINE": 1667,
    "HATCH": 3,
    "LWPOLYLINE": 4,
    "LEADER": 23,
    "INSERT": 3,
    "CIRCLE": 18,
    "ARC": 47,
    "SPLINE": 2,
    "TEXT": 6,
    "MTEXT": 23,
    "DIMENSION": 23
  },
  "geometry_checksum": 3625044934656.0,
  "bounds": [
    [
      278340.34,
      -2066.46
    ],
    [
      283537.69,
      -904.64
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
