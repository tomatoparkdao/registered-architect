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
    "SPLINE": 2,
    "LWPOLYLINE": 27,
    "HATCH": 1,
    "LINE": 39,
    "ELLIPSE": 4,
    "CIRCLE": 1,
    "ARC": 6
  },
  "geometry_checksum": 109016176.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      1060.0,
      2180.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
