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
    "LINE": 60,
    "LWPOLYLINE": 8,
    "HATCH": 1,
    "TEXT": 7,
    "DIMENSION": 10
  },
  "geometry_checksum": 250688176.0,
  "bounds": [
    [
      1060.68,
      1904.53
    ],
    [
      3852.79,
      3519.53
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
