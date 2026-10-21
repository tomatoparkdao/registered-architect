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
    "LWPOLYLINE": 500,
    "LINE": 1397,
    "HATCH": 8,
    "INSERT": 69,
    "CIRCLE": 200,
    "ARC": 780,
    "SPLINE": 108,
    "TEXT": 116,
    "DIMENSION": 72
  },
  "geometry_checksum": -112917643001856.0,
  "bounds": [
    [
      -1750240.5,
      -1826726.0
    ],
    [
      -1689979.25,
      -1793278.62
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
