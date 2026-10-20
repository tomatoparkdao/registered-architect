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
    "SOLID": 14,
    "ARC": 6,
    "LINE": 87,
    "CIRCLE": 1,
    "INSERT": 3,
    "LWPOLYLINE": 1,
    "TEXT": 18
  },
  "geometry_checksum": 18208332.0,
  "bounds": [
    [
      -54.43,
      0.0
    ],
    [
      195.84,
      382.85
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
