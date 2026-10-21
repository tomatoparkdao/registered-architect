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
    "LINE": 507,
    "HATCH": 13,
    "CIRCLE": 9,
    "INSERT": 42,
    "ELLIPSE": 18,
    "LWPOLYLINE": 3,
    "TEXT": 65
  },
  "geometry_checksum": 2384019712.0,
  "bounds": [
    [
      199.48,
      -126.77
    ],
    [
      1379.99,
      1391.79
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
