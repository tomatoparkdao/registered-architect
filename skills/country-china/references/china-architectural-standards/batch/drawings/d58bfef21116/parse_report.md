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
    "LINE": 23,
    "ARC": 2,
    "CIRCLE": 6,
    "LWPOLYLINE": 1,
    "HATCH": 2,
    "SPLINE": 1,
    "ELLIPSE": 1
  },
  "geometry_checksum": -12527420.0,
  "bounds": [
    [
      -4672.62,
      0.0
    ],
    [
      -3752.62,
      2100.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
