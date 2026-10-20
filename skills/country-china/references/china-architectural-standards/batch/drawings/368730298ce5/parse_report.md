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
    "INSERT": 3,
    "LINE": 87,
    "ARC": 3,
    "LWPOLYLINE": 2,
    "CIRCLE": 2,
    "SOLID": 25,
    "TEXT": 40
  },
  "geometry_checksum": 45756712.0,
  "bounds": [
    [
      -9.51,
      0.0
    ],
    [
      400.86,
      288.42
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
