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
    "ARC": 50,
    "LINE": 402,
    "INSERT": 7,
    "CIRCLE": 3,
    "SOLID": 76,
    "LWPOLYLINE": 8,
    "TEXT": 104
  },
  "geometry_checksum": 967919360.0,
  "bounds": [
    [
      -47.0,
      -5.0
    ],
    [
      564.11,
      408.72
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
