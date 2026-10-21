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
    "LWPOLYLINE": 190,
    "LINE": 833,
    "CIRCLE": 9,
    "HATCH": 15,
    "ARC": 1,
    "INSERT": 143,
    "ELLIPSE": 2,
    "TEXT": 105
  },
  "geometry_checksum": 61290188800.0,
  "bounds": [
    [
      883.5,
      -2035.84
    ],
    [
      11306.46,
      10833.99
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
