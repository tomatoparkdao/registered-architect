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
    "LINE": 24,
    "INSERT": 8,
    "ARC": 2,
    "HATCH": 6,
    "LEADER": 9,
    "LWPOLYLINE": 4,
    "TEXT": 7,
    "MTEXT": 8,
    "DIMENSION": 9
  },
  "geometry_checksum": -2755576320.0,
  "bounds": [
    [
      -141793.03,
      -192627.73
    ],
    [
      191453.56,
      250032.28
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
