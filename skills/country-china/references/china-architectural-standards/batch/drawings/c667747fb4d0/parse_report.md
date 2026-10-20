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
    "LINE": 717,
    "CIRCLE": 26,
    "ARC": 117,
    "HATCH": 4,
    "INSERT": 26,
    "LWPOLYLINE": 25,
    "TEXT": 86,
    "MTEXT": 9
  },
  "geometry_checksum": 55169277952.0,
  "bounds": [
    [
      1743.01,
      9360.95
    ],
    [
      6808.36,
      13925.28
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
