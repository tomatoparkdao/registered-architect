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
    "LINE": 833,
    "CIRCLE": 10,
    "LWPOLYLINE": 16,
    "ARC": 56,
    "INSERT": 6,
    "SPLINE": 4,
    "HATCH": 2,
    "TEXT": 101
  },
  "geometry_checksum": 51289018368.0,
  "bounds": [
    [
      4582.05,
      4400.68
    ],
    [
      10369.9,
      9717.61
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
