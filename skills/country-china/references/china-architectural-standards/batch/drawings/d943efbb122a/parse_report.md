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
    "LINE": 85,
    "LWPOLYLINE": 5,
    "ARC": 6,
    "HATCH": 2,
    "TEXT": 8,
    "DIMENSION": 3
  },
  "geometry_checksum": -254552304.0,
  "bounds": [
    [
      -4717.49,
      131.74
    ],
    [
      -3712.72,
      1029.17
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
