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
    "LINE": 442,
    "INSERT": 18,
    "CIRCLE": 14,
    "ARC": 6,
    "SOLID": 8,
    "LWPOLYLINE": 40,
    "TEXT": 19
  },
  "geometry_checksum": 59235324919808.0,
  "bounds": [
    [
      3179310.25,
      2037378.38
    ],
    [
      3366739.5,
      2265270.25
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
