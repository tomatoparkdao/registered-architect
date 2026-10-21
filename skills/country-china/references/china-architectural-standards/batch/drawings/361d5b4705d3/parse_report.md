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
    "LINE": 192,
    "HATCH": 10,
    "LWPOLYLINE": 24,
    "INSERT": 3,
    "CIRCLE": 4,
    "TEXT": 21,
    "DIMENSION": 24
  },
  "geometry_checksum": 34431348736.0,
  "bounds": [
    [
      28235.98,
      35621.71
    ],
    [
      38266.67,
      40935.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
