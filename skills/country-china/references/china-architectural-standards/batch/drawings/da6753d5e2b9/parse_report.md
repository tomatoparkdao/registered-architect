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
    "LEADER": 15,
    "LINE": 598,
    "HATCH": 14,
    "LWPOLYLINE": 28,
    "CIRCLE": 2,
    "INSERT": 2,
    "ARC": 42,
    "MTEXT": 3,
    "TEXT": 16,
    "DIMENSION": 5
  },
  "geometry_checksum": 53765263360.0,
  "bounds": [
    [
      25120.91,
      -8738.38
    ],
    [
      32823.3,
      -5571.73
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
