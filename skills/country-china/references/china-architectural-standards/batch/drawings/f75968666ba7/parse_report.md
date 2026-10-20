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
    "LEADER": 41,
    "LINE": 2352,
    "LWPOLYLINE": 61,
    "HATCH": 18,
    "CIRCLE": 6,
    "ARC": 67,
    "INSERT": 6,
    "TEXT": 54,
    "DIMENSION": 71
  },
  "geometry_checksum": 213640577024.0,
  "bounds": [
    [
      201.56,
      190.45
    ],
    [
      4967.08,
      6927.48
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
