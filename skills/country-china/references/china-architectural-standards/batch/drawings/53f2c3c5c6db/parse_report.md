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
    "LEADER": 30,
    "HATCH": 18,
    "LINE": 289,
    "LWPOLYLINE": 44,
    "ARC": 79,
    "CIRCLE": 4,
    "TEXT": 48,
    "DIMENSION": 100
  },
  "geometry_checksum": 23927404544.0,
  "bounds": [
    [
      109.23,
      146.09
    ],
    [
      5141.41,
      7044.04
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
