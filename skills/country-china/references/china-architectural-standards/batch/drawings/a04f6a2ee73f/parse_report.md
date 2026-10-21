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
    "LINE": 902,
    "INSERT": 6,
    "LWPOLYLINE": 303,
    "HATCH": 11,
    "ELLIPSE": 1,
    "ARC": 2,
    "CIRCLE": 1,
    "MTEXT": 4,
    "TEXT": 144,
    "DIMENSION": 10
  },
  "geometry_checksum": -435974569984.0,
  "bounds": [
    [
      -16181.71,
      -8518.99
    ],
    [
      -7781.71,
      -2063.26
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
