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
    "LINE": 1057,
    "LWPOLYLINE": 4,
    "INSERT": 12,
    "CIRCLE": 6,
    "ARC": 88,
    "HATCH": 10,
    "ELLIPSE": 20,
    "TEXT": 76
  },
  "geometry_checksum": 11738783744.0,
  "bounds": [
    [
      -889842.12,
      -159624.56
    ],
    [
      891044.62,
      917585.19
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
