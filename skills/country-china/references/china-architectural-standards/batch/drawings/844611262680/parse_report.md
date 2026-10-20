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
    "LEADER": 28,
    "LWPOLYLINE": 22,
    "LINE": 2022,
    "HATCH": 15,
    "CIRCLE": 10,
    "ARC": 24,
    "TEXT": 57,
    "DIMENSION": 30
  },
  "geometry_checksum": 162700017664.0,
  "bounds": [
    [
      36.66,
      254.5
    ],
    [
      5290.52,
      6973.16
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
