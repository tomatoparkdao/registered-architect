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
    "CIRCLE": 15,
    "LINE": 263,
    "LWPOLYLINE": 13,
    "INSERT": 82,
    "HATCH": 5,
    "ARC": 1,
    "MTEXT": 230,
    "TEXT": 1,
    "DIMENSION": 11
  },
  "geometry_checksum": 29486366720.0,
  "bounds": [
    [
      -3732.35,
      -2.83
    ],
    [
      63.32,
      35481.33
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
