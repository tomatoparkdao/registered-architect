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
    "LINE": 69,
    "CIRCLE": 12,
    "INSERT": 1,
    "SOLID": 29,
    "ARC": 22,
    "LWPOLYLINE": 1,
    "TEXT": 33
  },
  "geometry_checksum": 56092656.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      556.52,
      397.29
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
