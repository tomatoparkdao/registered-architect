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
    "LEADER": 29,
    "LWPOLYLINE": 101,
    "CIRCLE": 4,
    "LINE": 678,
    "HATCH": 4,
    "ARC": 37,
    "INSERT": 28,
    "TEXT": 48,
    "DIMENSION": 30
  },
  "geometry_checksum": 116846198784.0,
  "bounds": [
    [
      -17826.56,
      -11307.86
    ],
    [
      7598992.0,
      9361.93
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
