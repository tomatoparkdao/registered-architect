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
    "LINE": 162,
    "ARC": 48,
    "LWPOLYLINE": 15,
    "HATCH": 5,
    "SPLINE": 1,
    "CIRCLE": 10,
    "LEADER": 11,
    "INSERT": 3,
    "MTEXT": 12,
    "TEXT": 4,
    "DIMENSION": 14
  },
  "geometry_checksum": 39184535552.0,
  "bounds": [
    [
      148121.66,
      -41318.84
    ],
    [
      153123.47,
      -30909.93
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
