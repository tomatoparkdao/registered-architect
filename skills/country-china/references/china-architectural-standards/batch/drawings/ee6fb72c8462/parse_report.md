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
    "CIRCLE": 5,
    "LINE": 74,
    "ARC": 10,
    "SOLID": 14,
    "LWPOLYLINE": 3,
    "INSERT": 5,
    "TEXT": 23
  },
  "geometry_checksum": 19960352.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      202.81,
      290.56
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
