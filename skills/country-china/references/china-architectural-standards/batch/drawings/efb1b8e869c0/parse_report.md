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
    "LINE": 403,
    "HATCH": 124,
    "CIRCLE": 125,
    "INSERT": 24,
    "LEADER": 4,
    "ARC": 89,
    "LWPOLYLINE": 21,
    "SPLINE": 2,
    "TEXT": 30
  },
  "geometry_checksum": 7606383104.0,
  "bounds": [
    [
      751.78,
      840.92
    ],
    [
      2441.95,
      1705.76
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
