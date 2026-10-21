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
    "LINE": 498,
    "LWPOLYLINE": 107,
    "HATCH": 12,
    "INSERT": 13,
    "ARC": 9,
    "CIRCLE": 2,
    "TEXT": 61,
    "DIMENSION": 55
  },
  "geometry_checksum": 186469072896.0,
  "bounds": [
    [
      0.0,
      -17518.52
    ],
    [
      59070.7,
      14272.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
