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
    "LINE": 192,
    "SOLID": 47,
    "ARC": 65,
    "INSERT": 6,
    "CIRCLE": 3,
    "LWPOLYLINE": 3,
    "TEXT": 64
  },
  "geometry_checksum": 274361376.0,
  "bounds": [
    [
      -15.64,
      0.0
    ],
    [
      567.28,
      407.98
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
