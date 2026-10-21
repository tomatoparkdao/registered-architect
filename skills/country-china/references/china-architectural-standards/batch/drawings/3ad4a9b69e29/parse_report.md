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
    "INSERT": 12,
    "LINE": 94,
    "HATCH": 9,
    "ARC": 2,
    "LWPOLYLINE": 8,
    "LEADER": 8,
    "CIRCLE": 1,
    "TEXT": 5,
    "MTEXT": 13,
    "DIMENSION": 2
  },
  "geometry_checksum": 17636749312.0,
  "bounds": [
    [
      211646.75,
      4303.16
    ],
    [
      215088.02,
      6922.42
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
