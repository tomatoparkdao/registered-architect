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
    "LINE": 135,
    "INSERT": 5,
    "LWPOLYLINE": 49,
    "ARC": 23,
    "CIRCLE": 7,
    "HATCH": 3,
    "TEXT": 28
  },
  "geometry_checksum": 184745824.0,
  "bounds": [
    [
      199.38,
      -128.41
    ],
    [
      318.25,
      74.97
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
