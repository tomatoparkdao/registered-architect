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
    "HATCH": 8,
    "LINE": 198,
    "CIRCLE": 40,
    "LWPOLYLINE": 42,
    "SPLINE": 6,
    "INSERT": 26,
    "MTEXT": 19,
    "TEXT": 2
  },
  "geometry_checksum": 6362993664.0,
  "bounds": [
    [
      5560.6,
      1823.81
    ],
    [
      7536.44,
      4372.28
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
