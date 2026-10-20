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
    "LINE": 328,
    "CIRCLE": 7,
    "ARC": 33,
    "INSERT": 7,
    "LWPOLYLINE": 2,
    "SOLID": 64,
    "TEXT": 92
  },
  "geometry_checksum": 685267776.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      810.43,
      582.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
