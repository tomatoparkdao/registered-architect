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
    "LINE": 2614,
    "HATCH": 22,
    "INSERT": 20,
    "LEADER": 59,
    "ARC": 411,
    "LWPOLYLINE": 21,
    "SPLINE": 21,
    "CIRCLE": 6,
    "TEXT": 48,
    "MTEXT": 40,
    "DIMENSION": 33
  },
  "geometry_checksum": -7123249397760.0,
  "bounds": [
    [
      -116297.84,
      -71556.03
    ],
    [
      -111680.03,
      -67922.17
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
