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
    "LINE": 382,
    "INSERT": 73,
    "LWPOLYLINE": 2,
    "CIRCLE": 1,
    "HATCH": 2,
    "TEXT": 99
  },
  "geometry_checksum": 5072627957760.0,
  "bounds": [
    [
      3221873.5,
      2273537.5
    ],
    [
      3272096.25,
      2298553.75
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
