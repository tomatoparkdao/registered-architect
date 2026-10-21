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
    "LINE": 32,
    "LWPOLYLINE": 5,
    "HATCH": 1,
    "TEXT": 5,
    "DIMENSION": 4
  },
  "geometry_checksum": 1590218.5,
  "bounds": [
    [
      -2480.0,
      1013.26
    ],
    [
      -1050.0,
      2320.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
