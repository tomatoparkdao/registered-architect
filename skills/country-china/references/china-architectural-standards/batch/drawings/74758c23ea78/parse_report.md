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
    "LINE": 384,
    "SOLID": 66,
    "CIRCLE": 3,
    "ARC": 47,
    "INSERT": 8,
    "LWPOLYLINE": 2,
    "TEXT": 80
  },
  "geometry_checksum": 677638144.0,
  "bounds": [
    [
      -207.31,
      -129.46
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
