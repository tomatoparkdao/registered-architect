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
    "ARC": 29,
    "CIRCLE": 4,
    "LINE": 246,
    "HATCH": 9,
    "INSERT": 11,
    "LWPOLYLINE": 4,
    "TEXT": 36
  },
  "geometry_checksum": 7732497408.0,
  "bounds": [
    [
      2383.25,
      2586.78
    ],
    [
      11520.8,
      6433.76
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
