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
    "LWPOLYLINE": 154,
    "CIRCLE": 9,
    "HATCH": 27,
    "LEADER": 23,
    "ARC": 17,
    "LINE": 4524,
    "INSERT": 9,
    "TEXT": 32,
    "DIMENSION": 49
  },
  "geometry_checksum": 526542667776.0,
  "bounds": [
    [
      -424.43,
      346.9
    ],
    [
      5814.03,
      5742.35
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
