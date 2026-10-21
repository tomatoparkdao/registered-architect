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
    "LINE": 281,
    "HATCH": 9,
    "LWPOLYLINE": 2,
    "LEADER": 15,
    "INSERT": 2,
    "ARC": 32,
    "CIRCLE": 12,
    "SPLINE": 2,
    "TEXT": 5,
    "MTEXT": 15,
    "DIMENSION": 9
  },
  "geometry_checksum": 172716687360.0,
  "bounds": [
    [
      286555.03,
      1878.18
    ],
    [
      289625.19,
      5356.62
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
