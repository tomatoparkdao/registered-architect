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
    "LINE": 956,
    "INSERT": 46,
    "CIRCLE": 28,
    "LWPOLYLINE": 12,
    "ARC": 17,
    "SPLINE": 1,
    "TEXT": 113,
    "MTEXT": 23,
    "DIMENSION": 1
  },
  "geometry_checksum": 85077704704.0,
  "bounds": [
    [
      -491.82,
      9423.15
    ],
    [
      9133.61,
      13500.9
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
