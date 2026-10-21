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
    "CIRCLE": 1528,
    "ARC": 3410,
    "LINE": 3829,
    "LWPOLYLINE": 156,
    "HATCH": 5,
    "LEADER": 25,
    "TEXT": 44,
    "DIMENSION": 46
  },
  "geometry_checksum": 1143440801792.0,
  "bounds": [
    [
      45.84,
      147.45
    ],
    [
      4087.11,
      5886.41
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
