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
    "ARC": 35,
    "INSERT": 1,
    "LINE": 42,
    "CIRCLE": 2,
    "SOLID": 28,
    "TEXT": 31
  },
  "geometry_checksum": 20237836.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      188.77,
      289.97
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
