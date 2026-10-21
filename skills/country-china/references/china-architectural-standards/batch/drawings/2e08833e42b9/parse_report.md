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
    "LINE": 150,
    "CIRCLE": 48,
    "ARC": 141,
    "LWPOLYLINE": 32,
    "LEADER": 7,
    "TEXT": 5,
    "MTEXT": 2,
    "DIMENSION": 11
  },
  "geometry_checksum": 2743617024.0,
  "bounds": [
    [
      -1025.23,
      -713.85
    ],
    [
      7015.37,
      1962.84
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
