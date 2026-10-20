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
    "LINE": 96,
    "SOLID": 29,
    "ARC": 1,
    "LWPOLYLINE": 13,
    "CIRCLE": 2,
    "TEXT": 41
  },
  "geometry_checksum": 49365824.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      191.66,
      290.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
