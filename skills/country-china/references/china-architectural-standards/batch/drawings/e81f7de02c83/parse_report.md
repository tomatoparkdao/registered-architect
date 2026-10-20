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
    "INSERT": 4,
    "LINE": 85,
    "LWPOLYLINE": 11,
    "SOLID": 29,
    "ARC": 3,
    "CIRCLE": 2,
    "TEXT": 38
  },
  "geometry_checksum": 42136112.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      189.28,
      290.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
