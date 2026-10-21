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
    "LINE": 260,
    "HATCH": 6,
    "INSERT": 47,
    "ARC": 4,
    "CIRCLE": 16,
    "LWPOLYLINE": 4,
    "TEXT": 56
  },
  "geometry_checksum": 42847666176.0,
  "bounds": [
    [
      38331.0,
      17797.6
    ],
    [
      59561.68,
      39790.95
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
