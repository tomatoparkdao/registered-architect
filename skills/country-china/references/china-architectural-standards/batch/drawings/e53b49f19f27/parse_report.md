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
    "LINE": 42,
    "CIRCLE": 2,
    "HATCH": 4,
    "LWPOLYLINE": 7,
    "INSERT": 1,
    "TEXT": 11,
    "DIMENSION": 6
  },
  "geometry_checksum": 400738112.0,
  "bounds": [
    [
      11261.73,
      5015.9
    ],
    [
      13051.17,
      7316.82
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
