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
    "LINE": 44,
    "INSERT": 8,
    "LWPOLYLINE": 7,
    "ARC": 2,
    "CIRCLE": 1,
    "HATCH": 8,
    "TEXT": 8,
    "MTEXT": 4,
    "DIMENSION": 10
  },
  "geometry_checksum": -12879902720.0,
  "bounds": [
    [
      -897131.19,
      -33333.82
    ],
    [
      610.0,
      316959.62
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
