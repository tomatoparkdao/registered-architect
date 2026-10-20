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
    "LWPOLYLINE": 981,
    "INSERT": 37,
    "LINE": 1037,
    "HATCH": 109,
    "ARC": 63,
    "CIRCLE": 22,
    "SPLINE": 74,
    "MTEXT": 4,
    "TEXT": 170,
    "DIMENSION": 70
  },
  "geometry_checksum": -2381974077440.0,
  "bounds": [
    [
      -87800.12,
      23832.58
    ],
    [
      -80290.12,
      29777.58
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
