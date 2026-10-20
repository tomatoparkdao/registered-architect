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
    "LINE": 433,
    "LWPOLYLINE": 141,
    "LEADER": 30,
    "CIRCLE": 6,
    "HATCH": 14,
    "ARC": 68,
    "TEXT": 45,
    "DIMENSION": 44
  },
  "geometry_checksum": 42051969024.0,
  "bounds": [
    [
      54.44,
      333.75
    ],
    [
      4991.98,
      7029.02
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
