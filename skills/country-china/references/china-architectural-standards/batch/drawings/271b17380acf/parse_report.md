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
    "LINE": 249,
    "INSERT": 1,
    "SOLID": 42,
    "CIRCLE": 2,
    "LWPOLYLINE": 4,
    "ARC": 4,
    "TEXT": 72
  },
  "geometry_checksum": 233813056.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      404.23,
      289.34
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
