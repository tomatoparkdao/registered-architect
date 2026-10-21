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
    "LWPOLYLINE": 64,
    "ARC": 95,
    "CIRCLE": 27,
    "HATCH": 30,
    "LINE": 258,
    "INSERT": 17,
    "TEXT": 42
  },
  "geometry_checksum": 1708269109248.0,
  "bounds": [
    [
      60459.62,
      3095.03
    ],
    [
      115004.41,
      80446.46
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
