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
    "LWPOLYLINE": 153,
    "LINE": 599,
    "HATCH": 68,
    "ARC": 44,
    "CIRCLE": 7,
    "TEXT": 146,
    "DIMENSION": 25
  },
  "geometry_checksum": 542267670528.0,
  "bounds": [
    [
      29335.01,
      -43401.82
    ],
    [
      113473.01,
      15676.73
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
