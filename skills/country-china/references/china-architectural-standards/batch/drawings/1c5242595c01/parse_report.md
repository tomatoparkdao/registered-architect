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
    "INSERT": 3,
    "LINE": 137,
    "CIRCLE": 14,
    "ARC": 18,
    "SOLID": 33,
    "LWPOLYLINE": 2,
    "TEXT": 52
  },
  "geometry_checksum": 115709824.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      557.82,
      392.61
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
