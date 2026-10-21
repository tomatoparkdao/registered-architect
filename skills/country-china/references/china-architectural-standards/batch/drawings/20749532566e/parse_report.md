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
    "LWPOLYLINE": 3,
    "LINE": 868,
    "ARC": 71,
    "HATCH": 11,
    "INSERT": 105,
    "CIRCLE": 12,
    "TEXT": 117
  },
  "geometry_checksum": 637999775744.0,
  "bounds": [
    [
      4925.4,
      -8334.75
    ],
    [
      108134.95,
      43599.48
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
