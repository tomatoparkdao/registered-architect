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
    "HATCH": 147,
    "LINE": 11232,
    "CIRCLE": 137,
    "SOLID": 135,
    "ARC": 136,
    "INSERT": 2334,
    "LWPOLYLINE": 226,
    "TEXT": 746,
    "MTEXT": 1165
  },
  "geometry_checksum": 6861133185024.0,
  "bounds": [
    [
      21047.24,
      -1736039.0
    ],
    [
      171251.62,
      -53717.55
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
