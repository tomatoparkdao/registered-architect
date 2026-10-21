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
    "LINE": 347,
    "HATCH": 5,
    "CIRCLE": 5,
    "ARC": 7,
    "LWPOLYLINE": 14,
    "TEXT": 115
  },
  "geometry_checksum": 39720816640.0,
  "bounds": [
    [
      31510.17,
      -3669.39
    ],
    [
      50517.86,
      22530.61
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
