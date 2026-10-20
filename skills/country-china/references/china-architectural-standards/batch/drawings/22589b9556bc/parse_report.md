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
    "LINE": 330,
    "SOLID": 55,
    "ARC": 25,
    "INSERT": 4,
    "CIRCLE": 5,
    "LWPOLYLINE": 3,
    "TEXT": 76
  },
  "geometry_checksum": 550529664.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      562.81,
      408.43
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
