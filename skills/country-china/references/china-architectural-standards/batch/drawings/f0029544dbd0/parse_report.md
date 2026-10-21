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
    "LINE": 421,
    "LWPOLYLINE": 35,
    "SPLINE": 2,
    "ARC": 9,
    "HATCH": 21,
    "CIRCLE": 9,
    "INSERT": 28,
    "TEXT": 49,
    "MTEXT": 11
  },
  "geometry_checksum": 489655369728.0,
  "bounds": [
    [
      111440.04,
      38549.05
    ],
    [
      111929.3,
      39183.26
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
