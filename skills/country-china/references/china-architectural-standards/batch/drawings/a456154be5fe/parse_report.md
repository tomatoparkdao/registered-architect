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
    "SPLINE": 304,
    "ARC": 443,
    "LWPOLYLINE": 61,
    "LINE": 188,
    "CIRCLE": 16,
    "HATCH": 1
  },
  "geometry_checksum": -1625197184.0,
  "bounds": [
    [
      -4769.12,
      39.86
    ],
    [
      -808.78,
      2152.37
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
