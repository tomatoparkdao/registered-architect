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
    "LEADER": 35,
    "LWPOLYLINE": 157,
    "LINE": 262,
    "ARC": 59,
    "CIRCLE": 16,
    "HATCH": 23,
    "TEXT": 49,
    "DIMENSION": 11
  },
  "geometry_checksum": 4956965888.0,
  "bounds": [
    [
      25.29,
      39.46
    ],
    [
      832.07,
      1138.67
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
