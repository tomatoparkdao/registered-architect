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
    "INSERT": 2,
    "LWPOLYLINE": 2,
    "LINE": 65,
    "SOLID": 22,
    "ARC": 2,
    "TEXT": 35
  },
  "geometry_checksum": 26209840.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      186.92,
      290.75
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
