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
    "LINE": 331,
    "HATCH": 10,
    "ARC": 36,
    "CIRCLE": 3,
    "LWPOLYLINE": 2,
    "SPLINE": 1,
    "INSERT": 18,
    "MTEXT": 21,
    "TEXT": 2
  },
  "geometry_checksum": 5101723648.0,
  "bounds": [
    [
      2883.69,
      3505.67
    ],
    [
      3784.21,
      4431.7
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
