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
    "LWPOLYLINE": 20,
    "LINE": 188,
    "SPLINE": 3,
    "ARC": 24,
    "HATCH": 7,
    "LEADER": 13,
    "TEXT": 4,
    "MTEXT": 15
  },
  "geometry_checksum": 25846317056.0,
  "bounds": [
    [
      -200828.16,
      7819.04
    ],
    [
      171097.98,
      9830.22
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
