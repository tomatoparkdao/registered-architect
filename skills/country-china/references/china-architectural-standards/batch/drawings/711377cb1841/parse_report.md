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
    "LEADER": 46,
    "HATCH": 51,
    "LINE": 860,
    "LWPOLYLINE": 274,
    "ARC": 114,
    "CIRCLE": 14,
    "ELLIPSE": 12,
    "TEXT": 98,
    "MTEXT": 2,
    "DIMENSION": 56
  },
  "geometry_checksum": 108735561728.0,
  "bounds": [
    [
      -173.23,
      -4355.79
    ],
    [
      18654.33,
      14625.7
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
