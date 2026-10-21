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
    "LINE": 75,
    "LWPOLYLINE": 4,
    "SPLINE": 8,
    "ARC": 4,
    "LEADER": 14,
    "HATCH": 2,
    "CIRCLE": 4,
    "MTEXT": 11,
    "TEXT": 4,
    "DIMENSION": 7
  },
  "geometry_checksum": 17728217088.0,
  "bounds": [
    [
      218110.62,
      3577.17
    ],
    [
      219825.31,
      4702.59
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
