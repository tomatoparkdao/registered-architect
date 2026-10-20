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
    "LEADER": 49,
    "CIRCLE": 10,
    "HATCH": 14,
    "LINE": 1764,
    "ARC": 12,
    "LWPOLYLINE": 34,
    "INSERT": 21,
    "TEXT": 62,
    "DIMENSION": 66
  },
  "geometry_checksum": 237519306752.0,
  "bounds": [
    [
      48.38,
      184.95
    ],
    [
      8586.56,
      11402.61
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
