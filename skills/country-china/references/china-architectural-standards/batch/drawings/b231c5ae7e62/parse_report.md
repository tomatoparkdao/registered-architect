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
    "INSERT": 4,
    "LINE": 102,
    "SOLID": 29,
    "LWPOLYLINE": 9,
    "CIRCLE": 3,
    "ARC": 3,
    "TEXT": 43
  },
  "geometry_checksum": 51615328.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      193.23,
      290.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
