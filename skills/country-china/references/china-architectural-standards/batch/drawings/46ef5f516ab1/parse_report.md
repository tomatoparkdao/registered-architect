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
    "ARC": 23,
    "LINE": 102,
    "CIRCLE": 8,
    "LWPOLYLINE": 45,
    "HATCH": 9,
    "INSERT": 3,
    "SOLID": 19,
    "TEXT": 24
  },
  "geometry_checksum": 325738624.0,
  "bounds": [
    [
      -21183.08,
      -1641.55
    ],
    [
      902.15,
      1034.32
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
