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
    "LEADER": 13,
    "LWPOLYLINE": 172,
    "ARC": 285,
    "LINE": 122,
    "HATCH": 6,
    "ELLIPSE": 14,
    "POLYLINE": 70,
    "CIRCLE": 14,
    "TEXT": 13
  },
  "geometry_checksum": 548397121536.0,
  "bounds": [
    [
      -3219.83,
      645.61
    ],
    [
      12339.52,
      18519.24
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
