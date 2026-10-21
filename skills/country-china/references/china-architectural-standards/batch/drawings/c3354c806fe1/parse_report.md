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
    "HATCH": 33,
    "ARC": 212,
    "LINE": 1715,
    "INSERT": 47,
    "LWPOLYLINE": 121,
    "CIRCLE": 52,
    "SOLID": 19,
    "SPLINE": 1,
    "TEXT": 265,
    "MTEXT": 6,
    "DIMENSION": 269
  },
  "geometry_checksum": 16946609258496.0,
  "bounds": [
    [
      -351516.28,
      -877401.56
    ],
    [
      452551.69,
      99887.95
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
