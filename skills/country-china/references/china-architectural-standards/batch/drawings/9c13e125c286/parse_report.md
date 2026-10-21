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
    "LEADER": 5,
    "LINE": 114,
    "HATCH": 6,
    "INSERT": 2,
    "ARC": 12,
    "LWPOLYLINE": 9,
    "CIRCLE": 1,
    "TEXT": 4,
    "MTEXT": 5,
    "DIMENSION": 7
  },
  "geometry_checksum": 9523288064.0,
  "bounds": [
    [
      52562.84,
      6735.56
    ],
    [
      53218.41,
      7451.78
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
