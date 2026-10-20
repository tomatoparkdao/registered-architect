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
    "LWPOLYLINE": 189,
    "CIRCLE": 168,
    "LINE": 51,
    "HATCH": 1,
    "ELLIPSE": 2,
    "ARC": 4
  },
  "geometry_checksum": -7049482752.0,
  "bounds": [
    [
      -9347.94,
      46.18
    ],
    [
      -6047.95,
      3829.53
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
