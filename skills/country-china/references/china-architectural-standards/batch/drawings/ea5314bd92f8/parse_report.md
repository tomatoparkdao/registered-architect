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
    "LEADER": 47,
    "CIRCLE": 6,
    "LWPOLYLINE": 47,
    "HATCH": 17,
    "LINE": 1724,
    "ARC": 6,
    "INSERT": 19,
    "TEXT": 60,
    "DIMENSION": 72
  },
  "geometry_checksum": 193561821184.0,
  "bounds": [
    [
      204.46,
      226.75
    ],
    [
      8126.51,
      19558.53
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
