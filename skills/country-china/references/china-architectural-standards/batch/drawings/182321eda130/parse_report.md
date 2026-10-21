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
    "LINE": 252,
    "INSERT": 8,
    "HATCH": 48,
    "LWPOLYLINE": 88,
    "CIRCLE": 23,
    "TEXT": 42,
    "DIMENSION": 81
  },
  "geometry_checksum": 47654723584.0,
  "bounds": [
    [
      7389.2,
      -3661.31
    ],
    [
      18249.5,
      11696.68
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
