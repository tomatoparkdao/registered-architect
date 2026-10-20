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
    "LINE": 791,
    "ARC": 60,
    "INSERT": 2,
    "CIRCLE": 12,
    "LWPOLYLINE": 15,
    "HATCH": 4,
    "TEXT": 84
  },
  "geometry_checksum": 38631645184.0,
  "bounds": [
    [
      174.01,
      6657.51
    ],
    [
      7274.89,
      9970.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
