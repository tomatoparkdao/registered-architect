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
    "ARC": 33,
    "LINE": 252,
    "CIRCLE": 8,
    "HATCH": 4,
    "SPLINE": 4,
    "MTEXT": 93
  },
  "geometry_checksum": Infinity,
  "bounds": [
    [
      4795.51,
      0.0
    ],
    [
      Infinity,
      2931.27
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
