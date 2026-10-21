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
    "LEADER": 1,
    "LINE": 753,
    "LWPOLYLINE": 99,
    "HATCH": 6,
    "ARC": 175,
    "CIRCLE": 4,
    "SPLINE": 4,
    "TEXT": 6,
    "DIMENSION": 56
  },
  "geometry_checksum": 76162596864.0,
  "bounds": [
    [
      130.36,
      4379.75
    ],
    [
      5284.5,
      7131.79
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
