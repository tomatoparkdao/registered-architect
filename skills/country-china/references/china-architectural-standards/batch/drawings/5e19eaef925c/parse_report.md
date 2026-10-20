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
    "INSERT": 86,
    "LINE": 2657,
    "LWPOLYLINE": 171,
    "LEADER": 31,
    "CIRCLE": 4,
    "HATCH": 17,
    "ARC": 15,
    "TEXT": 43,
    "DIMENSION": 69
  },
  "geometry_checksum": 409649086464.0,
  "bounds": [
    [
      97.79,
      155.56
    ],
    [
      5549.64,
      7021.89
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
