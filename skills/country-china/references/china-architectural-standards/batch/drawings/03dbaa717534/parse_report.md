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
    "LWPOLYLINE": 608,
    "LINE": 2494,
    "INSERT": 8,
    "HATCH": 73,
    "ARC": 1379,
    "CIRCLE": 18,
    "SPLINE": 37,
    "ELLIPSE": 1,
    "TEXT": 128,
    "MTEXT": 5
  },
  "geometry_checksum": 79315091456.0,
  "bounds": [
    [
      -3003.11,
      130.74
    ],
    [
      626.1,
      925.24
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
