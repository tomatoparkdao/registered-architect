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
    "LWPOLYLINE": 53,
    "HATCH": 43,
    "LINE": 555,
    "CIRCLE": 23,
    "INSERT": 20,
    "ARC": 4,
    "ELLIPSE": 2,
    "TEXT": 190,
    "DIMENSION": 72
  },
  "geometry_checksum": -142068170752.0,
  "bounds": [
    [
      -52038.28,
      11225.06
    ],
    [
      -39438.28,
      20135.06
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
