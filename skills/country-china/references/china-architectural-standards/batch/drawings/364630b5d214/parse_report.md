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
    "LINE": 380,
    "CIRCLE": 42,
    "LWPOLYLINE": 101,
    "ARC": 201,
    "HATCH": 15,
    "LEADER": 4,
    "SOLID": 6,
    "INSERT": 50,
    "TEXT": 128
  },
  "geometry_checksum": 10833742848.0,
  "bounds": [
    [
      320.71,
      -3656.46
    ],
    [
      21875.25,
      34741.81
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
