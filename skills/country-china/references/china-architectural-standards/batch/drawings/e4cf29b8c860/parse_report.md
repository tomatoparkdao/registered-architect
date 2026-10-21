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
    "LINE": 2145,
    "HATCH": 52,
    "ELLIPSE": 8,
    "ARC": 98,
    "CIRCLE": 6,
    "LWPOLYLINE": 13,
    "LEADER": 1,
    "INSERT": 64,
    "TEXT": 33,
    "MTEXT": 38
  },
  "geometry_checksum": 5643790450688.0,
  "bounds": [
    [
      74951.13,
      -101750.86
    ],
    [
      351644.53,
      260088.59
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
