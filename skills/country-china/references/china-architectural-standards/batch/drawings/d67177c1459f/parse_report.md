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
    "INSERT": 2,
    "LINE": 79,
    "CIRCLE": 2,
    "SOLID": 19,
    "ARC": 3,
    "TEXT": 29
  },
  "geometry_checksum": 27363844.0,
  "bounds": [
    [
      -10.0,
      0.0
    ],
    [
      402.32,
      278.36
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
