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
    "LINE": 2359,
    "ARC": 174,
    "LWPOLYLINE": 18,
    "CIRCLE": 14,
    "HATCH": 70,
    "ELLIPSE": 7,
    "INSERT": 67,
    "LEADER": 1,
    "TEXT": 39,
    "MTEXT": 39
  },
  "geometry_checksum": 19158934749184.0,
  "bounds": [
    [
      341731.19,
      -76407.33
    ],
    [
      604892.25,
      262869.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
