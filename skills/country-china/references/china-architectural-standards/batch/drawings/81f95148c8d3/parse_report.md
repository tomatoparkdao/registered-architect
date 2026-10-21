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
    "LINE": 704,
    "CIRCLE": 6,
    "ELLIPSE": 36,
    "INSERT": 41,
    "HATCH": 4,
    "TEXT": 73
  },
  "geometry_checksum": -666694848.0,
  "bounds": [
    [
      -706719.06,
      -676703.5
    ],
    [
      708727.31,
      110885.05
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
