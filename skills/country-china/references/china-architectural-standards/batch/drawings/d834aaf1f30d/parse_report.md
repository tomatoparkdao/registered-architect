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
    "LINE": 209,
    "LWPOLYLINE": 1,
    "CIRCLE": 22,
    "SOLID": 40,
    "ARC": 2,
    "TEXT": 42
  },
  "geometry_checksum": 303146240.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      813.17,
      582.95
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
