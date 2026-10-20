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
    "LINE": 525,
    "ARC": 190,
    "LWPOLYLINE": 378,
    "HATCH": 6,
    "LEADER": 31,
    "CIRCLE": 252,
    "INSERT": 3,
    "TEXT": 51,
    "DIMENSION": 43
  },
  "geometry_checksum": 98028027904.0,
  "bounds": [
    [
      -151.23,
      -2650.89
    ],
    [
      9293.62,
      7348.12
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
