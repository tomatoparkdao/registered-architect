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
    "LWPOLYLINE": 220,
    "LINE": 21297,
    "CIRCLE": 10,
    "LEADER": 39,
    "ARC": 36,
    "HATCH": 4,
    "INSERT": 80,
    "TEXT": 99
  },
  "geometry_checksum": 17531392753664.0,
  "bounds": [
    [
      1598.06,
      1096.64
    ],
    [
      9095.55,
      10651.1
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
