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
    "LINE": 500,
    "HATCH": 2,
    "INSERT": 1,
    "LEADER": 10,
    "SPLINE": 67,
    "ARC": 24,
    "CIRCLE": 6,
    "TEXT": 3,
    "MTEXT": 9,
    "DIMENSION": 25
  },
  "geometry_checksum": 424672952320.0,
  "bounds": [
    [
      299239.78,
      2731.84
    ],
    [
      305456.91,
      5320.77
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
