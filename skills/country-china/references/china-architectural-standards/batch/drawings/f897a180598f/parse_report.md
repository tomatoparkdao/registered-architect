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
    "LWPOLYLINE": 12,
    "LINE": 101,
    "SOLID": 37,
    "INSERT": 2,
    "ARC": 1,
    "CIRCLE": 1,
    "TEXT": 52
  },
  "geometry_checksum": 56727760.0,
  "bounds": [
    [
      -23.72,
      0.0
    ],
    [
      184.77,
      290.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
