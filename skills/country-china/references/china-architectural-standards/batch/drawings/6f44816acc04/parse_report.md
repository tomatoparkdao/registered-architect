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
    "ARC": 64,
    "LINE": 370,
    "INSERT": 7,
    "CIRCLE": 6,
    "SOLID": 79,
    "LWPOLYLINE": 3,
    "TEXT": 102
  },
  "geometry_checksum": 603567744.0,
  "bounds": [
    [
      -11.06,
      -37.67
    ],
    [
      409.81,
      296.11
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
