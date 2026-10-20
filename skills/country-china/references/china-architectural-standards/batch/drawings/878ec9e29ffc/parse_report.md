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
    "LWPOLYLINE": 84,
    "LINE": 1590,
    "CIRCLE": 42,
    "INSERT": 3,
    "TEXT": 75,
    "DIMENSION": 2
  },
  "geometry_checksum": 91215055814656.0,
  "bounds": [
    [
      3274447.25,
      2272729.0
    ],
    [
      3299181.75,
      2301777.75
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
