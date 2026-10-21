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
    "LINE": 487,
    "CIRCLE": 2,
    "HATCH": 6,
    "ELLIPSE": 21,
    "INSERT": 75,
    "ARC": 1,
    "TEXT": 68
  },
  "geometry_checksum": 3091643392.0,
  "bounds": [
    [
      -132617.19,
      -291597.0
    ],
    [
      488463.12,
      390719.34
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
