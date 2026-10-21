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
    "LINE": 21071,
    "LWPOLYLINE": 217,
    "HATCH": 3,
    "LEADER": 40,
    "CIRCLE": 11,
    "ARC": 35,
    "TEXT": 48,
    "DIMENSION": 52
  },
  "geometry_checksum": 19690508255232.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      7267.55,
      9545.13
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
