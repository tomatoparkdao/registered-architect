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
    "LINE": 824,
    "LWPOLYLINE": 157,
    "ARC": 16,
    "CIRCLE": 28,
    "HATCH": 45,
    "ELLIPSE": 2,
    "INSERT": 31,
    "TEXT": 183,
    "MTEXT": 10,
    "DIMENSION": 80
  },
  "geometry_checksum": -174262484992.0,
  "bounds": [
    [
      -42380.55,
      -10711.16
    ],
    [
      -380.55,
      32828.95
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
