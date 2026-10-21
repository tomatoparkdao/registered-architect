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
    "LINE": 52,
    "LWPOLYLINE": 11,
    "INSERT": 2,
    "SPLINE": 1,
    "TEXT": 8,
    "DIMENSION": 14
  },
  "geometry_checksum": 537893.0,
  "bounds": [
    [
      -2770.53,
      1277.12
    ],
    [
      -710.12,
      2220.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
