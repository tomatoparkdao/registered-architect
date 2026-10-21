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
    "LINE": 917,
    "ARC": 258,
    "LWPOLYLINE": 44,
    "CIRCLE": 10,
    "HATCH": 37,
    "INSERT": 43,
    "ELLIPSE": 1,
    "LEADER": 3,
    "TEXT": 26,
    "MTEXT": 28
  },
  "geometry_checksum": 41555476480.0,
  "bounds": [
    [
      -3313.35,
      1266.27
    ],
    [
      3828.73,
      2593.48
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
