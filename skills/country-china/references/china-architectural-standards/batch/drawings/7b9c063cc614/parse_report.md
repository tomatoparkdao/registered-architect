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
    "LINE": 1559,
    "LWPOLYLINE": 153,
    "ARC": 121,
    "INSERT": 246,
    "POLYLINE": 23,
    "HATCH": 54,
    "CIRCLE": 40,
    "SPLINE": 4,
    "MTEXT": 27,
    "TEXT": 22
  },
  "geometry_checksum": -8338600886272.0,
  "bounds": [
    [
      -528673.75,
      172572.39
    ],
    [
      528584.88,
      173513.41
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
