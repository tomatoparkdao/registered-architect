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
    "LINE": 356,
    "CIRCLE": 1,
    "ARC": 48,
    "INSERT": 8,
    "LWPOLYLINE": 2,
    "SOLID": 67,
    "TEXT": 77
  },
  "geometry_checksum": 573866880.0,
  "bounds": [
    [
      0.0,
      0.0
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
