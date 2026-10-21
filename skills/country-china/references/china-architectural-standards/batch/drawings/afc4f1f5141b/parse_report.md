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
    "LINE": 1090,
    "INSERT": 109,
    "LWPOLYLINE": 97,
    "CIRCLE": 5,
    "ARC": 45,
    "HATCH": 20,
    "SPLINE": 6,
    "TEXT": 193,
    "DIMENSION": 203
  },
  "geometry_checksum": 4393520857088.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      252374.55,
      108740.85
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
