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
    "LWPOLYLINE": 25,
    "INSERT": 5,
    "LINE": 1077,
    "LEADER": 25,
    "HATCH": 3,
    "CIRCLE": 10,
    "TEXT": 18,
    "MTEXT": 25,
    "DIMENSION": 25
  },
  "geometry_checksum": 245206859776.0,
  "bounds": [
    [
      40297.21,
      -4151.54
    ],
    [
      42909.06,
      1086.21
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
