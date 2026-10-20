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
    "ARC": 16,
    "LINE": 124,
    "CIRCLE": 9,
    "LWPOLYLINE": 2,
    "SOLID": 31,
    "INSERT": 3,
    "TEXT": 45
  },
  "geometry_checksum": 83781392.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      390.24,
      288.12
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
