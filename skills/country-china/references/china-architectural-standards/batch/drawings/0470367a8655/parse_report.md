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
    "LEADER": 34,
    "HATCH": 8,
    "LWPOLYLINE": 84,
    "CIRCLE": 8,
    "LINE": 121,
    "ARC": 75,
    "TEXT": 53,
    "DIMENSION": 90
  },
  "geometry_checksum": 15565922304.0,
  "bounds": [
    [
      -957.92,
      196.66
    ],
    [
      5860.31,
      7003.22
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
