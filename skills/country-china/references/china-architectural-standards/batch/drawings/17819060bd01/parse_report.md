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
    "LWPOLYLINE": 17,
    "LINE": 849,
    "CIRCLE": 6,
    "INSERT": 7,
    "ARC": 5,
    "SOLID": 5,
    "TEXT": 25,
    "DIMENSION": 8
  },
  "geometry_checksum": 164991205376.0,
  "bounds": [
    [
      1491.25,
      -12784.08
    ],
    [
      64669.53,
      5794.96
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
