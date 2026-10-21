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
    "CIRCLE": 39,
    "LINE": 887,
    "ARC": 40,
    "HATCH": 5,
    "LWPOLYLINE": 7,
    "SOLID": 3,
    "INSERT": 127,
    "TEXT": 102,
    "MTEXT": 64
  },
  "geometry_checksum": 48828047360.0,
  "bounds": [
    [
      63097.24,
      -83417.55
    ],
    [
      105147.24,
      -53717.55
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
