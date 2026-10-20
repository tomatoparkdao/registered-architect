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
    "INSERT": 4,
    "CIRCLE": 4,
    "LINE": 89,
    "SOLID": 18,
    "ARC": 7,
    "TEXT": 33
  },
  "geometry_checksum": 25858056.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      402.81,
      290.05
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
