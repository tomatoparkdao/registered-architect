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
    "LINE": 805,
    "LWPOLYLINE": 2,
    "CIRCLE": 2,
    "ARC": 1,
    "INSERT": 57,
    "TEXT": 42
  },
  "geometry_checksum": 33999851520.0,
  "bounds": [
    [
      841.13,
      293.7
    ],
    [
      8072.68,
      9063.73
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
