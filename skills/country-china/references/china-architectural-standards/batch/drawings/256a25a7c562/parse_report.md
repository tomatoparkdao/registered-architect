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
    "LINE": 35,
    "LWPOLYLINE": 132,
    "HATCH": 1,
    "CIRCLE": 9,
    "ARC": 16,
    "SPLINE": 7
  },
  "geometry_checksum": -657542272.0,
  "bounds": [
    [
      -4571.62,
      35.43
    ],
    [
      -1931.62,
      3854.04
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
