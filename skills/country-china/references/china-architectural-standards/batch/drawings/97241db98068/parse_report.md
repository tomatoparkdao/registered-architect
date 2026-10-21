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
    "LINE": 3550,
    "LWPOLYLINE": 564,
    "INSERT": 127,
    "HATCH": 119,
    "ARC": 257,
    "CIRCLE": 21,
    "ELLIPSE": 4,
    "TEXT": 119,
    "MTEXT": 38
  },
  "geometry_checksum": 612919148544.0,
  "bounds": [
    [
      -26.18,
      924.56
    ],
    [
      7743.36,
      3258.46
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
