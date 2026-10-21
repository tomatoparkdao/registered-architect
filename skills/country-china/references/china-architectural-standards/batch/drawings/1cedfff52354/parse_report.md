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
    "LWPOLYLINE": 10,
    "LINE": 576,
    "CIRCLE": 20,
    "HATCH": 20,
    "INSERT": 14,
    "ARC": 62,
    "SPLINE": 1,
    "LEADER": 6,
    "MTEXT": 10,
    "DIMENSION": 23
  },
  "geometry_checksum": 6602543104.0,
  "bounds": [
    [
      -538.47,
      357.97
    ],
    [
      2882.97,
      2777.17
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
