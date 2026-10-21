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
    "LINE": 959,
    "LWPOLYLINE": 27,
    "INSERT": 2,
    "HATCH": 4,
    "TEXT": 22,
    "DIMENSION": 7
  },
  "geometry_checksum": -10884098048.0,
  "bounds": [
    [
      -5547.14,
      243.48
    ],
    [
      -2258.29,
      2640.3
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
