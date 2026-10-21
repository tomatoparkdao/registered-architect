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
    "LINE": 193,
    "LWPOLYLINE": 14,
    "HATCH": 9,
    "ARC": 3,
    "LEADER": 9,
    "CIRCLE": 7,
    "SPLINE": 1,
    "MTEXT": 9,
    "TEXT": 17,
    "DIMENSION": 36
  },
  "geometry_checksum": 29952165888.0,
  "bounds": [
    [
      53250.42,
      6215.93
    ],
    [
      57766.62,
      9464.26
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
