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
    "ARC": 45,
    "LINE": 295,
    "HATCH": 35,
    "LEADER": 28,
    "LWPOLYLINE": 163,
    "CIRCLE": 8,
    "TEXT": 56,
    "MTEXT": 2,
    "DIMENSION": 18
  },
  "geometry_checksum": 15188030464.0,
  "bounds": [
    [
      103.23,
      236.92
    ],
    [
      15302.49,
      11861.68
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
