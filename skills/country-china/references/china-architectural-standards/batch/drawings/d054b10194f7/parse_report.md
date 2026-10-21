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
    "INSERT": 9,
    "LINE": 422,
    "SOLID": 1,
    "CIRCLE": 27,
    "HATCH": 24,
    "LWPOLYLINE": 12,
    "ARC": 53,
    "MTEXT": 17,
    "TEXT": 1,
    "DIMENSION": 8
  },
  "geometry_checksum": 3601411584.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      724029.19,
      309406.72
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
