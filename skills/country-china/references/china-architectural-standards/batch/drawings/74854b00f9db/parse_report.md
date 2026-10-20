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
    "LINE": 243,
    "ARC": 74,
    "LWPOLYLINE": 6,
    "INSERT": 7,
    "CIRCLE": 3,
    "SOLID": 54,
    "TEXT": 67
  },
  "geometry_checksum": 665461120.0,
  "bounds": [
    [
      -156.19,
      -44.65
    ],
    [
      813.71,
      581.25
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
