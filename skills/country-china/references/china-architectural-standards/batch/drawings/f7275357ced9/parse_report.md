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
    "LINE": 529,
    "ARC": 55,
    "INSERT": 18,
    "CIRCLE": 2,
    "LWPOLYLINE": 6,
    "SOLID": 26,
    "TEXT": 49
  },
  "geometry_checksum": 987496640.0,
  "bounds": [
    [
      -156.29,
      0.0
    ],
    [
      811.81,
      590.41
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
