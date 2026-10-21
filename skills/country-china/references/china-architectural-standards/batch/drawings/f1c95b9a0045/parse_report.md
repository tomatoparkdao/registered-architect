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
    "LINE": 489,
    "ARC": 26,
    "HATCH": 5,
    "CIRCLE": 5,
    "LWPOLYLINE": 8,
    "INSERT": 35,
    "TEXT": 59
  },
  "geometry_checksum": 118757580800.0,
  "bounds": [
    [
      3088.64,
      16857.55
    ],
    [
      49266.19,
      90221.07
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
