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
    "LWPOLYLINE": 255,
    "LINE": 1131,
    "CIRCLE": 7,
    "ARC": 714,
    "ELLIPSE": 1,
    "SPLINE": 23,
    "INSERT": 2,
    "HATCH": 1,
    "TEXT": 64
  },
  "geometry_checksum": 57791176704.0,
  "bounds": [
    [
      -736.99,
      -2195.8
    ],
    [
      4954.98,
      2515.55
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
