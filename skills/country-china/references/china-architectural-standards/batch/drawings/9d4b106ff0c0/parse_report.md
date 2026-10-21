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
    "LINE": 16469,
    "INSERT": 280,
    "LWPOLYLINE": 780,
    "HATCH": 135,
    "SOLID": 22,
    "ELLIPSE": 239,
    "CIRCLE": 79,
    "ARC": 47,
    "TEXT": 1327,
    "DIMENSION": 803
  },
  "geometry_checksum": 929951821856768.0,
  "bounds": [
    [
      362854.72,
      48567.67
    ],
    [
      490031.84,
      114727.14
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
