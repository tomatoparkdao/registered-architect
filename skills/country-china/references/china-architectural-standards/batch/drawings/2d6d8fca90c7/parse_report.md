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
    "CIRCLE": 42,
    "LINE": 576,
    "ARC": 33,
    "LWPOLYLINE": 26,
    "INSERT": 5,
    "TEXT": 79,
    "MTEXT": 2,
    "DIMENSION": 2
  },
  "geometry_checksum": 29033521152.0,
  "bounds": [
    [
      3413.45,
      7131.18
    ],
    [
      9658.29,
      11098.79
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
