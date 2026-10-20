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
    "LINE": 809,
    "INSERT": 133,
    "LWPOLYLINE": 76,
    "LEADER": 37,
    "CIRCLE": 10,
    "HATCH": 7,
    "ARC": 4,
    "TEXT": 64,
    "DIMENSION": 38
  },
  "geometry_checksum": 187524448256.0,
  "bounds": [
    [
      187.09,
      -146.03
    ],
    [
      15113030.0,
      9336.61
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
