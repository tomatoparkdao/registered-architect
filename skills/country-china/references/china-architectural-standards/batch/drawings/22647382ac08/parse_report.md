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
    "LWPOLYLINE": 8,
    "HATCH": 6,
    "LINE": 56,
    "INSERT": 2,
    "LEADER": 5,
    "CIRCLE": 1,
    "ARC": 4,
    "MTEXT": 5,
    "TEXT": 8,
    "DIMENSION": 16
  },
  "geometry_checksum": 12647641088.0,
  "bounds": [
    [
      217873.31,
      5424.71
    ],
    [
      220072.52,
      6396.99
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
