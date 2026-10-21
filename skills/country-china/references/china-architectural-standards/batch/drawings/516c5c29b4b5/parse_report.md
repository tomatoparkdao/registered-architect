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
    "LINE": 992,
    "ARC": 433,
    "INSERT": 5,
    "LWPOLYLINE": 118,
    "CIRCLE": 3,
    "ELLIPSE": 81,
    "POLYLINE": 2,
    "TEXT": 70,
    "DIMENSION": 130
  },
  "geometry_checksum": -5013163008.0,
  "bounds": [
    [
      -311.77,
      -21.95
    ],
    [
      -304.1,
      -16.61
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
