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
    "INSERT": 2,
    "LWPOLYLINE": 13,
    "LINE": 63,
    "CIRCLE": 4,
    "LEADER": 3,
    "ARC": 5,
    "MTEXT": 7,
    "DIMENSION": 1
  },
  "geometry_checksum": 9569857536.0,
  "bounds": [
    [
      262608.81,
      -24516.24
    ],
    [
      263961.81,
      -22778.6
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
