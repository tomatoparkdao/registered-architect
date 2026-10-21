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
    "LINE": 705,
    "INSERT": 112,
    "HATCH": 14,
    "LWPOLYLINE": 2,
    "CIRCLE": 12,
    "ARC": 2,
    "TEXT": 119
  },
  "geometry_checksum": 2177792475136.0,
  "bounds": [
    [
      116593.09,
      460660.78
    ],
    [
      142933.77,
      494305.38
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
