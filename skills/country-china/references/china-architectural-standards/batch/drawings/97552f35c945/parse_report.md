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
    "SPLINE": 325,
    "LWPOLYLINE": 82,
    "LINE": 194,
    "HATCH": 7,
    "ARC": 325,
    "CIRCLE": 5,
    "ELLIPSE": 2
  },
  "geometry_checksum": 2548325376.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      1500.0,
      2300.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
