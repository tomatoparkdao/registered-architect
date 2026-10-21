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
    "LINE": 4440,
    "CIRCLE": 14,
    "HATCH": 57,
    "LEADER": 31,
    "ARC": 48,
    "INSERT": 7,
    "LWPOLYLINE": 31,
    "TEXT": 41,
    "DIMENSION": 8
  },
  "geometry_checksum": 30448747020288.0,
  "bounds": [
    [
      179534.77,
      160716.38
    ],
    [
      194312.27,
      185645.48
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
