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
    "LINE": 138,
    "ARC": 16,
    "CIRCLE": 4,
    "INSERT": 5,
    "SOLID": 23,
    "LWPOLYLINE": 3,
    "TEXT": 40
  },
  "geometry_checksum": 64027036.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      188.9,
      290.38
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
