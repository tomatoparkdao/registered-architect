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
    "SOLID": 35,
    "LINE": 125,
    "ARC": 15,
    "CIRCLE": 4,
    "INSERT": 5,
    "LWPOLYLINE": 2,
    "TEXT": 49
  },
  "geometry_checksum": 130883504.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      565.83,
      408.67
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
