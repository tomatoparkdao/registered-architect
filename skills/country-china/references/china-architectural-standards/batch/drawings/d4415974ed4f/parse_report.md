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
    "LINE": 2089,
    "ARC": 35,
    "LWPOLYLINE": 66,
    "LEADER": 21,
    "HATCH": 10,
    "CIRCLE": 8,
    "INSERT": 18,
    "TEXT": 33,
    "DIMENSION": 44
  },
  "geometry_checksum": 122935353344.0,
  "bounds": [
    [
      44.84,
      67.08
    ],
    [
      3505.35,
      4677.99
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
