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
    "LINE": 343,
    "HATCH": 6,
    "LWPOLYLINE": 31,
    "CIRCLE": 26,
    "INSERT": 49,
    "TEXT": 82
  },
  "geometry_checksum": 27586721792.0,
  "bounds": [
    [
      240.71,
      -1434.58
    ],
    [
      30971.04,
      32642.49
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
