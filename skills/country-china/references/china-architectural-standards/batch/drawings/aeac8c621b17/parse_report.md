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
    "LINE": 318,
    "ARC": 17,
    "LEADER": 7,
    "CIRCLE": 5,
    "HATCH": 13,
    "LWPOLYLINE": 16,
    "INSERT": 46,
    "ELLIPSE": 3,
    "TEXT": 40
  },
  "geometry_checksum": 1706765312.0,
  "bounds": [
    [
      925.06,
      430.68
    ],
    [
      1888.32,
      880.38
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
