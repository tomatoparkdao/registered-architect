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
    "LWPOLYLINE": 3,
    "HATCH": 33,
    "LINE": 327,
    "CIRCLE": 4,
    "ARC": 4,
    "INSERT": 56,
    "TEXT": 63
  },
  "geometry_checksum": 58802749440.0,
  "bounds": [
    [
      -3738.58,
      -5087.31
    ],
    [
      54731.91,
      25763.96
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
