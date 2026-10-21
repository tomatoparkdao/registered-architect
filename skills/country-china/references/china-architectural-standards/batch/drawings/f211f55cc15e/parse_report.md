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
    "CIRCLE": 14,
    "LINE": 365,
    "ARC": 24,
    "INSERT": 50,
    "TEXT": 76
  },
  "geometry_checksum": 8287180800.0,
  "bounds": [
    [
      -19.95,
      -1836469.0
    ],
    [
      2262532.0,
      11450.01
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
