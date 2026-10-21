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
    "LWPOLYLINE": 755,
    "LINE": 1422,
    "CIRCLE": 7,
    "ARC": 1189,
    "ELLIPSE": 1,
    "HATCH": 47,
    "SPLINE": 37,
    "INSERT": 2,
    "TEXT": 327
  },
  "geometry_checksum": 139426447360.0,
  "bounds": [
    [
      -736.99,
      -2195.8
    ],
    [
      4954.98,
      2515.55
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
