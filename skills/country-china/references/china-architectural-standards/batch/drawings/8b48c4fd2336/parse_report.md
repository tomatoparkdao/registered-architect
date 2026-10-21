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
    "LWPOLYLINE": 50,
    "LINE": 1967,
    "LEADER": 51,
    "INSERT": 102,
    "HATCH": 11,
    "CIRCLE": 6,
    "ARC": 1,
    "TEXT": 106
  },
  "geometry_checksum": 269994541056.0,
  "bounds": [
    [
      1597.09,
      689.54
    ],
    [
      10891.43,
      12582.9
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
