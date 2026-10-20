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
    "LINE": 349,
    "ARC": 44,
    "CIRCLE": 26,
    "LWPOLYLINE": 8,
    "INSERT": 14,
    "SOLID": 18,
    "TEXT": 54
  },
  "geometry_checksum": 487214784.0,
  "bounds": [
    [
      -20.7,
      0.0
    ],
    [
      569.68,
      393.86
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
