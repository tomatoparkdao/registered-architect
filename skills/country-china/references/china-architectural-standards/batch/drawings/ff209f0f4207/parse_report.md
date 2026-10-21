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
    "CIRCLE": 4,
    "LINE": 1552,
    "INSERT": 7,
    "ARC": 3,
    "HATCH": 1,
    "SOLID": 3,
    "TEXT": 39
  },
  "geometry_checksum": 85124251648.0,
  "bounds": [
    [
      -1136.04,
      -8783.38
    ],
    [
      13898.33,
      14677.97
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
