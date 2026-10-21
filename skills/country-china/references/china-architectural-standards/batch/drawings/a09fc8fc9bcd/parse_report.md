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
    "LINE": 364,
    "INSERT": 48,
    "ELLIPSE": 12,
    "CIRCLE": 4,
    "HATCH": 2,
    "ARC": 1,
    "TEXT": 55
  },
  "geometry_checksum": 902973568.0,
  "bounds": [
    [
      -230022.67,
      -677193.31
    ],
    [
      1564.49,
      678812.06
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
