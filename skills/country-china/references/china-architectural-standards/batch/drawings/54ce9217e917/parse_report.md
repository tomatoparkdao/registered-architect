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
    "LINE": 1847,
    "CIRCLE": 74,
    "INSERT": 314,
    "LWPOLYLINE": 21,
    "SOLID": 9,
    "ARC": 8,
    "TEXT": 113,
    "MTEXT": 157
  },
  "geometry_checksum": 9227486625792.0,
  "bounds": [
    [
      436269.25,
      -9460.15
    ],
    [
      478319.25,
      20239.85
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
