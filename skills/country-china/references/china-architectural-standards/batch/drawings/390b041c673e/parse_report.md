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
    "LINE": 135,
    "INSERT": 6,
    "ARC": 6,
    "SOLID": 29,
    "CIRCLE": 5,
    "LWPOLYLINE": 3,
    "TEXT": 42
  },
  "geometry_checksum": 70405784.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      393.31,
      268.12
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
