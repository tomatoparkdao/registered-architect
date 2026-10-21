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
    "LINE": 335,
    "ARC": 13,
    "LWPOLYLINE": 16,
    "CIRCLE": 13,
    "LEADER": 7,
    "HATCH": 7,
    "TEXT": 12,
    "DIMENSION": 28
  },
  "geometry_checksum": 5505317376.0,
  "bounds": [
    [
      -1322.58,
      3147.89
    ],
    [
      3379.35,
      4726.67
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
