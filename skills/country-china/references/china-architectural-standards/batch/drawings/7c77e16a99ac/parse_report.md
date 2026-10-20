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
    "LEADER": 22,
    "ARC": 34,
    "LINE": 170,
    "LWPOLYLINE": 160,
    "CIRCLE": 8,
    "HATCH": 7,
    "INSERT": 1,
    "TEXT": 28,
    "MTEXT": 1,
    "DIMENSION": 66
  },
  "geometry_checksum": 20188942336.0,
  "bounds": [
    [
      -1251.51,
      0.0
    ],
    [
      5383.48,
      7000.64
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
