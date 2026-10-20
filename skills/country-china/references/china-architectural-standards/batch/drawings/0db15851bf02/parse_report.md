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
    "LINE": 309,
    "SOLID": 59,
    "CIRCLE": 3,
    "ARC": 41,
    "INSERT": 7,
    "LWPOLYLINE": 2,
    "TEXT": 75
  },
  "geometry_checksum": 463807488.0,
  "bounds": [
    [
      -190.67,
      -281.99
    ],
    [
      578.17,
      409.45
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
