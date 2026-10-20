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
    "LINE": 749,
    "CIRCLE": 5,
    "HATCH": 15,
    "LWPOLYLINE": 115,
    "LEADER": 26,
    "POLYLINE": 46,
    "ARC": 1,
    "TEXT": 9,
    "MTEXT": 37,
    "DIMENSION": 44
  },
  "geometry_checksum": 43816939520.0,
  "bounds": [
    [
      45.55,
      221.69
    ],
    [
      3440.95,
      4651.42
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
