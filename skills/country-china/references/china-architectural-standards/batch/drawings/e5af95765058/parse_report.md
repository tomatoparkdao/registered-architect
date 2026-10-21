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
    "LWPOLYLINE": 1,
    "HATCH": 13,
    "LINE": 517,
    "INSERT": 20,
    "CIRCLE": 3,
    "TEXT": 56
  },
  "geometry_checksum": 109121224704.0,
  "bounds": [
    [
      5034.6,
      -4517.87
    ],
    [
      58364.68,
      26333.39
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
