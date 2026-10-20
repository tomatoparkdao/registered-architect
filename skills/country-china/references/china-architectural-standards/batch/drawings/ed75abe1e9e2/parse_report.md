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
    "LINE": 79,
    "CIRCLE": 10,
    "INSERT": 5,
    "SOLID": 22,
    "ARC": 8,
    "TEXT": 38
  },
  "geometry_checksum": 45357548.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      553.46,
      386.71
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
