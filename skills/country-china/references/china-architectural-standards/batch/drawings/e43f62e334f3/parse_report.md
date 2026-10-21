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
    "LINE": 1999,
    "LWPOLYLINE": 2,
    "CIRCLE": 35,
    "HATCH": 6,
    "INSERT": 13,
    "TEXT": 260,
    "MTEXT": 1
  },
  "geometry_checksum": -255025659904.0,
  "bounds": [
    [
      -14038.03,
      -46972.0
    ],
    [
      57009.94,
      11966.14
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
