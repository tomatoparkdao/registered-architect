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
    "SOLID": 20,
    "LINE": 687,
    "INSERT": 42,
    "LWPOLYLINE": 8,
    "ARC": 45,
    "CIRCLE": 4,
    "TEXT": 59
  },
  "geometry_checksum": 1154203392.0,
  "bounds": [
    [
      -45.04,
      -109.23
    ],
    [
      534.44,
      406.37
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
