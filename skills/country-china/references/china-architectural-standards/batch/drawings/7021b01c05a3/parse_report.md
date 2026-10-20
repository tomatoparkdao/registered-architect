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
    "ARC": 75,
    "INSERT": 5,
    "LINE": 211,
    "CIRCLE": 3,
    "SOLID": 58,
    "LWPOLYLINE": 2,
    "TEXT": 60
  },
  "geometry_checksum": 259011488.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      392.03,
      288.86
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
