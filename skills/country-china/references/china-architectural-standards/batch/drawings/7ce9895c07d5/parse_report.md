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
    "LINE": 715,
    "LWPOLYLINE": 101,
    "INSERT": 42,
    "HATCH": 11,
    "CIRCLE": 20,
    "ARC": 21,
    "SOLID": 3,
    "TEXT": 95,
    "MTEXT": 15,
    "DIMENSION": 63
  },
  "geometry_checksum": 812391989248.0,
  "bounds": [
    [
      163825.52,
      -74600.07
    ],
    [
      205875.52,
      -44900.07
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
