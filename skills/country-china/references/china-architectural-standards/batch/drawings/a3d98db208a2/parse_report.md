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
    "CIRCLE": 7,
    "LINE": 114,
    "HATCH": 14,
    "LEADER": 9,
    "INSERT": 6,
    "ARC": 7,
    "TEXT": 7,
    "MTEXT": 10,
    "DIMENSION": 4
  },
  "geometry_checksum": 28588167168.0,
  "bounds": [
    [
      96467.78,
      -4977.21
    ],
    [
      97851.18,
      -4366.15
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
