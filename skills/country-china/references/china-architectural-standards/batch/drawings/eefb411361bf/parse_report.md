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
    "LINE": 331,
    "CIRCLE": 24,
    "HATCH": 12,
    "ARC": 158,
    "LWPOLYLINE": 12,
    "ELLIPSE": 3,
    "INSERT": 26,
    "TEXT": 16,
    "MTEXT": 13
  },
  "geometry_checksum": 5598298112.0,
  "bounds": [
    [
      -3641.65,
      1992.92
    ],
    [
      4269.64,
      2737.22
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
