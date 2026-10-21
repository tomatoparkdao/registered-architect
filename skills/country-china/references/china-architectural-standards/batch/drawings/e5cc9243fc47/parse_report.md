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
    "LINE": 249,
    "LWPOLYLINE": 45,
    "CIRCLE": 8,
    "HATCH": 23,
    "SPLINE": 4,
    "ARC": 8,
    "INSERT": 3,
    "TEXT": 39,
    "DIMENSION": 34
  },
  "geometry_checksum": 22857310208.0,
  "bounds": [
    [
      952.37,
      10114.73
    ],
    [
      6640.51,
      14137.06
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
