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
    "LINE": 49,
    "LWPOLYLINE": 16,
    "INSERT": 1,
    "CIRCLE": 4,
    "TEXT": 33,
    "DIMENSION": 4
  },
  "geometry_checksum": 15697602.0,
  "bounds": [
    [
      -3487.04,
      -24185.05
    ],
    [
      5482.31,
      3624.97
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
