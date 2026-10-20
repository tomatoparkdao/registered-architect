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
    "LINE": 105,
    "SOLID": 31,
    "INSERT": 4,
    "ARC": 3,
    "LWPOLYLINE": 13,
    "CIRCLE": 2,
    "TEXT": 42
  },
  "geometry_checksum": 56226768.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      194.03,
      290.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
