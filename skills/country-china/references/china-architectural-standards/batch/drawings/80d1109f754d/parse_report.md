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
    "LINE": 1080,
    "LWPOLYLINE": 443,
    "CIRCLE": 58,
    "HATCH": 18,
    "LEADER": 31,
    "ELLIPSE": 1,
    "ARC": 2,
    "TEXT": 54,
    "DIMENSION": 81
  },
  "geometry_checksum": 324536631296.0,
  "bounds": [
    [
      6298.92,
      -54.23
    ],
    [
      8055.65,
      2209.77
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
