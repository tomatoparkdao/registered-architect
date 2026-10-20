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
    "INSERT": 24,
    "LINE": 627,
    "HATCH": 6,
    "ARC": 84,
    "CIRCLE": 29,
    "LWPOLYLINE": 18,
    "TEXT": 83,
    "MTEXT": 3,
    "DIMENSION": 2
  },
  "geometry_checksum": 45806362624.0,
  "bounds": [
    [
      3296.22,
      8336.48
    ],
    [
      8594.14,
      13334.88
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
