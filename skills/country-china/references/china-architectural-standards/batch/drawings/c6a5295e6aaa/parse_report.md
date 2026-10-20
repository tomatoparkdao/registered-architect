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
    "INSERT": 43,
    "LWPOLYLINE": 157,
    "LINE": 75,
    "SOLID": 24,
    "ARC": 4,
    "CIRCLE": 2,
    "TEXT": 87
  },
  "geometry_checksum": 533550272.0,
  "bounds": [
    [
      -340.0,
      -335.0
    ],
    [
      582.0,
      841.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
