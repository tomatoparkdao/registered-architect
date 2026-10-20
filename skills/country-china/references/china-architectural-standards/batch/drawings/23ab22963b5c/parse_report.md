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
    "LEADER": 27,
    "HATCH": 6,
    "ARC": 121,
    "LWPOLYLINE": 90,
    "LINE": 178,
    "CIRCLE": 4,
    "INSERT": 45,
    "TEXT": 40,
    "DIMENSION": 72
  },
  "geometry_checksum": 14106736640.0,
  "bounds": [
    [
      77.47,
      248.35
    ],
    [
      5030.98,
      6933.76
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
