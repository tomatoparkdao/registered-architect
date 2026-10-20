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
    "LINE": 1320,
    "ARC": 114,
    "CIRCLE": 94,
    "LWPOLYLINE": 124,
    "INSERT": 40,
    "SOLID": 4,
    "TEXT": 196,
    "DIMENSION": 380
  },
  "geometry_checksum": -7884470484992.0,
  "bounds": [
    [
      -259333.56,
      -94137.39
    ],
    [
      -195597.55,
      -64246.61
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
