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
    "LWPOLYLINE": 13,
    "LINE": 301,
    "CIRCLE": 2,
    "INSERT": 2,
    "TEXT": 11,
    "DIMENSION": 7
  },
  "geometry_checksum": 34945675264.0,
  "bounds": [
    [
      51424.43,
      5606.31
    ],
    [
      62005.46,
      17348.4
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
