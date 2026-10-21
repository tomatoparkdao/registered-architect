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
    "LINE": 512,
    "LWPOLYLINE": 90,
    "HATCH": 12,
    "ARC": 66,
    "LEADER": 4,
    "CIRCLE": 14,
    "INSERT": 84,
    "TEXT": 112
  },
  "geometry_checksum": 7569831936.0,
  "bounds": [
    [
      468.28,
      -872.76
    ],
    [
      3379.16,
      970.03
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
