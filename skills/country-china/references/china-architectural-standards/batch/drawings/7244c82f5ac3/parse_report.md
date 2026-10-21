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
    "LINE": 710,
    "LWPOLYLINE": 72,
    "ARC": 29,
    "HATCH": 10,
    "SPLINE": 1,
    "CIRCLE": 1,
    "TEXT": 124,
    "DIMENSION": 123
  },
  "geometry_checksum": 43543056384.0,
  "bounds": [
    [
      2560.0,
      -4690.0
    ],
    [
      14440.0,
      3710.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
