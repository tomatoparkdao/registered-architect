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
    "INSERT": 13,
    "LINE": 444,
    "ARC": 28,
    "HATCH": 8,
    "LWPOLYLINE": 62,
    "CIRCLE": 10,
    "ELLIPSE": 2,
    "MTEXT": 20,
    "TEXT": 6
  },
  "geometry_checksum": 22084857856.0,
  "bounds": [
    [
      7764.78,
      4064.82
    ],
    [
      9446.83,
      5388.6
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
