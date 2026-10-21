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
    "LINE": 741,
    "INSERT": 37,
    "HATCH": 46,
    "LWPOLYLINE": 65,
    "ELLIPSE": 264,
    "LEADER": 7,
    "CIRCLE": 4,
    "TEXT": 32,
    "DIMENSION": 20
  },
  "geometry_checksum": 791009558528.0,
  "bounds": [
    [
      297524.06,
      -508077.62
    ],
    [
      407057.0,
      116139.33
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
