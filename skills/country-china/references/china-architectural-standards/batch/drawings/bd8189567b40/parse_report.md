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
    "LWPOLYLINE": 57,
    "LINE": 402,
    "LEADER": 11,
    "CIRCLE": 9,
    "HATCH": 5,
    "SPLINE": 190,
    "INSERT": 30,
    "ARC": 4,
    "MTEXT": 28,
    "DIMENSION": 38
  },
  "geometry_checksum": 153433915392.0,
  "bounds": [
    [
      131111.73,
      -47277.63
    ],
    [
      135286.59,
      -44477.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
