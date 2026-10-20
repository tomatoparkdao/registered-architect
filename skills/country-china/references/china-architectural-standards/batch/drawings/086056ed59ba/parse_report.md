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
    "LWPOLYLINE": 132,
    "LINE": 4431,
    "HATCH": 2,
    "INSERT": 34,
    "CIRCLE": 96,
    "ARC": 8,
    "TEXT": 44
  },
  "geometry_checksum": 518127204958208.0,
  "bounds": [
    [
      3364256.0,
      2270615.75
    ],
    [
      3396190.5,
      2303889.5
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
