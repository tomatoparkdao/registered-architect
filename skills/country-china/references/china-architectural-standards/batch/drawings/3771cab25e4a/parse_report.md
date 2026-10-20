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
    "LINE": 345,
    "SOLID": 61,
    "CIRCLE": 12,
    "ARC": 56,
    "INSERT": 8,
    "TEXT": 82
  },
  "geometry_checksum": 490488448.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      395.0,
      289.32
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
