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
    "INSERT": 30,
    "LINE": 2042,
    "ARC": 904,
    "ELLIPSE": 3,
    "HATCH": 41,
    "LWPOLYLINE": 79,
    "CIRCLE": 8,
    "MTEXT": 35,
    "TEXT": 6
  },
  "geometry_checksum": 229620219904.0,
  "bounds": [
    [
      -3519.22,
      1251.89
    ],
    [
      3667.33,
      2549.79
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
