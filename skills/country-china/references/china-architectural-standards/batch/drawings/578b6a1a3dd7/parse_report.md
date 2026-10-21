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
    "LINE": 124,
    "INSERT": 2,
    "LWPOLYLINE": 5,
    "ARC": 13,
    "HATCH": 1,
    "CIRCLE": 30,
    "TEXT": 48,
    "DIMENSION": 17
  },
  "geometry_checksum": 439277952.0,
  "bounds": [
    [
      1589.94,
      -28240.0
    ],
    [
      10669.94,
      -240.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
