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
    "LINE": 264,
    "HATCH": 1,
    "LWPOLYLINE": 2,
    "CIRCLE": 8,
    "ARC": 24,
    "LEADER": 11,
    "SPLINE": 50,
    "TEXT": 3,
    "MTEXT": 11,
    "DIMENSION": 22
  },
  "geometry_checksum": 122336886784.0,
  "bounds": [
    [
      231591.48,
      -18680.68
    ],
    [
      286476.5,
      -2036.24
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
