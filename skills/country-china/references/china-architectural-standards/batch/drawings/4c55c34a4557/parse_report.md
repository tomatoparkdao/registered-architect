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
    "LINE": 4529,
    "HATCH": 318,
    "ARC": 230,
    "LWPOLYLINE": 104,
    "INSERT": 10,
    "CIRCLE": 28,
    "SPLINE": 10,
    "TEXT": 278,
    "MTEXT": 60,
    "DIMENSION": 8
  },
  "geometry_checksum": 98091424284672.0,
  "bounds": [
    [
      190969.75,
      -209723.14
    ],
    [
      978616.88,
      143078.38
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
