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
    "CIRCLE": 19,
    "LINE": 163,
    "LWPOLYLINE": 33,
    "ARC": 48,
    "ELLIPSE": 2,
    "LEADER": 23,
    "HATCH": 8,
    "INSERT": 2,
    "TEXT": 30,
    "MTEXT": 1,
    "DIMENSION": 19
  },
  "geometry_checksum": 691850304.0,
  "bounds": [
    [
      10.59,
      36.93
    ],
    [
      388.36,
      1174.66
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
