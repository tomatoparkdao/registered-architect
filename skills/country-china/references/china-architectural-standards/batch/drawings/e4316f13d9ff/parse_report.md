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
    "LINE": 1948,
    "INSERT": 3,
    "LWPOLYLINE": 16,
    "HATCH": 2,
    "ARC": 18,
    "TEXT": 23,
    "DIMENSION": 6
  },
  "geometry_checksum": 26010054656.0,
  "bounds": [
    [
      -1620.48,
      251.43
    ],
    [
      1650.86,
      2780.3
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
