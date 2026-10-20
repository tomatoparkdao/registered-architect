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
    "LINE": 98,
    "CIRCLE": 7,
    "INSERT": 2,
    "SOLID": 23,
    "ARC": 15,
    "TEXT": 34
  },
  "geometry_checksum": 43886936.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      394.51,
      263.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
