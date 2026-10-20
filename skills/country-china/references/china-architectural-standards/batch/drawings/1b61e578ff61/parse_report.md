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
    "LEADER": 25,
    "HATCH": 17,
    "LWPOLYLINE": 322,
    "LINE": 2578,
    "CIRCLE": 14,
    "ARC": 2,
    "TEXT": 42,
    "DIMENSION": 81
  },
  "geometry_checksum": 399064399872.0,
  "bounds": [
    [
      119.84,
      123.99
    ],
    [
      5367.14,
      7054.57
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
