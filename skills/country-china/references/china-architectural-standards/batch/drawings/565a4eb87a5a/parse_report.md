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
    "LINE": 323,
    "LWPOLYLINE": 6,
    "ARC": 47,
    "INSERT": 2,
    "HATCH": 4,
    "CIRCLE": 4,
    "TEXT": 27,
    "DIMENSION": 10
  },
  "geometry_checksum": -1828908800.0,
  "bounds": [
    [
      -6408.26,
      51.14
    ],
    [
      -863.11,
      2650.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
