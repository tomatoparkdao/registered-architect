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
    "LEADER": 24,
    "LINE": 444,
    "INSERT": 15,
    "LWPOLYLINE": 50,
    "HATCH": 15,
    "ARC": 6,
    "CIRCLE": 9,
    "POLYLINE": 1,
    "TEXT": 36,
    "DIMENSION": 33
  },
  "geometry_checksum": 17857613824.0,
  "bounds": [
    [
      -1769.19,
      322.64
    ],
    [
      7780.49,
      6910.94
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
