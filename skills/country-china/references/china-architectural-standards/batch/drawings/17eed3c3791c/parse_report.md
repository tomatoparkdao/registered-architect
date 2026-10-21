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
    "LINE": 565,
    "INSERT": 38,
    "SPLINE": 28,
    "LWPOLYLINE": 211,
    "HATCH": 56,
    "CIRCLE": 40,
    "ARC": 39,
    "ELLIPSE": 2,
    "POLYLINE": 527,
    "TEXT": 104,
    "DIMENSION": 118
  },
  "geometry_checksum": 15533133004800.0,
  "bounds": [
    [
      -1886423.38,
      -58755.82
    ],
    [
      2378432.0,
      1854760.75
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
