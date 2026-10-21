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
    "LINE": 575,
    "CIRCLE": 4,
    "ELLIPSE": 21,
    "INSERT": 60,
    "HATCH": 6,
    "LWPOLYLINE": 2,
    "ARC": 4,
    "TEXT": 76
  },
  "geometry_checksum": 7730444288.0,
  "bounds": [
    [
      -138080.66,
      -405158.34
    ],
    [
      570551.5,
      194101.41
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
