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
    "LINE": 1499,
    "LWPOLYLINE": 33,
    "HATCH": 16,
    "ARC": 68,
    "LEADER": 32,
    "INSERT": 14,
    "CIRCLE": 6,
    "TEXT": 45,
    "DIMENSION": 94
  },
  "geometry_checksum": 106905083904.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      5409.64,
      6872.05
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
