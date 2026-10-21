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
    "LINE": 399,
    "LWPOLYLINE": 42,
    "CIRCLE": 38,
    "LEADER": 11,
    "ARC": 9,
    "HATCH": 6,
    "TEXT": 17,
    "DIMENSION": 24
  },
  "geometry_checksum": 4696970240.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      3349.54,
      1418.99
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
