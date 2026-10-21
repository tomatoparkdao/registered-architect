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
    "LWPOLYLINE": 592,
    "ARC": 1425,
    "LINE": 2045,
    "CIRCLE": 16,
    "INSERT": 2,
    "HATCH": 81,
    "SPLINE": 37,
    "ELLIPSE": 1,
    "TEXT": 144,
    "MTEXT": 5
  },
  "geometry_checksum": 273705926656.0,
  "bounds": [
    [
      -2235.22,
      360.24
    ],
    [
      2066.72,
      1121.69
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
