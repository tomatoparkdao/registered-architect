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
    "HATCH": 12,
    "LINE": 247,
    "LWPOLYLINE": 59,
    "INSERT": 3,
    "ARC": 14,
    "TEXT": 25,
    "DIMENSION": 101
  },
  "geometry_checksum": 209777410048.0,
  "bounds": [
    [
      -12481.04,
      0.0
    ],
    [
      52205.56,
      156299.66
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
