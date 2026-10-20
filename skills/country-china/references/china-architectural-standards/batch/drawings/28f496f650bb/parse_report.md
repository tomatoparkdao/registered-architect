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
    "LINE": 1216,
    "HATCH": 16,
    "INSERT": 26,
    "LEADER": 37,
    "CIRCLE": 9,
    "LWPOLYLINE": 188,
    "ARC": 15,
    "TEXT": 50,
    "DIMENSION": 51
  },
  "geometry_checksum": -175926722560.0,
  "bounds": [
    [
      1429.38,
      -25969.98
    ],
    [
      9868.06,
      -14888.17
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
