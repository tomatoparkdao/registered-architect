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
    "LINE": 296,
    "HATCH": 2,
    "CIRCLE": 1,
    "LWPOLYLINE": 35,
    "ARC": 28,
    "INSERT": 8,
    "TEXT": 19
  },
  "geometry_checksum": 7427998720.0,
  "bounds": [
    [
      839.81,
      -12515.99
    ],
    [
      23194.77,
      21553.47
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
