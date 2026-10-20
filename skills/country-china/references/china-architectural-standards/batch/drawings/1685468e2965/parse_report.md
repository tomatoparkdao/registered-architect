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
    "ARC": 57,
    "LINE": 470,
    "CIRCLE": 2,
    "LWPOLYLINE": 8,
    "INSERT": 8,
    "SOLID": 96,
    "TEXT": 117
  },
  "geometry_checksum": 1711668480.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      813.49,
      582.28
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
