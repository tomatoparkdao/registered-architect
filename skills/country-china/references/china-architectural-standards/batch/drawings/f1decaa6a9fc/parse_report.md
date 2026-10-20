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
    "LWPOLYLINE": 31,
    "LINE": 760,
    "CIRCLE": 6,
    "INSERT": 2,
    "SOLID": 25,
    "ARC": 3,
    "TEXT": 23,
    "DIMENSION": 4
  },
  "geometry_checksum": 101652840448.0,
  "bounds": [
    [
      12877.21,
      7025.14
    ],
    [
      33595.19,
      16413.04
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
