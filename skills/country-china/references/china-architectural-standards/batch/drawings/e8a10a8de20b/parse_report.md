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
    "LINE": 2447,
    "ARC": 1373,
    "LWPOLYLINE": 609,
    "INSERT": 8,
    "HATCH": 83,
    "CIRCLE": 21,
    "SPLINE": 37,
    "ELLIPSE": 1,
    "TEXT": 132,
    "MTEXT": 5
  },
  "geometry_checksum": -77103964160.0,
  "bounds": [
    [
      -3990.71,
      217.92
    ],
    [
      -109.43,
      824.71
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
