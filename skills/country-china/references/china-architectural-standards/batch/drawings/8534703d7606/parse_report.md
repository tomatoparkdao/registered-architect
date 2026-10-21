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
    "INSERT": 1,
    "LINE": 201,
    "CIRCLE": 32,
    "ARC": 22,
    "LWPOLYLINE": 2,
    "TEXT": 34,
    "DIMENSION": 34
  },
  "geometry_checksum": 95123128320.0,
  "bounds": [
    [
      -119887.23,
      0.0
    ],
    [
      0.0,
      328124.06
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
