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
    "LINE": 72,
    "INSERT": 1,
    "LWPOLYLINE": 8,
    "ARC": 8,
    "HATCH": 2,
    "CIRCLE": 8,
    "TEXT": 38,
    "DIMENSION": 5
  },
  "geometry_checksum": 28821112.0,
  "bounds": [
    [
      -3533.02,
      -24150.0
    ],
    [
      5510.0,
      3690.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
