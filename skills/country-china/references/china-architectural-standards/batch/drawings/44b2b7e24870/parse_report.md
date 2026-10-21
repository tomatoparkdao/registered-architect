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
    "LINE": 508,
    "LWPOLYLINE": 108,
    "HATCH": 5,
    "CIRCLE": 7,
    "ARC": 1,
    "SPLINE": 1,
    "INSERT": 36,
    "TEXT": 64
  },
  "geometry_checksum": 225149452288.0,
  "bounds": [
    [
      -7783.81,
      81459.77
    ],
    [
      -3639.52,
      85290.84
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
