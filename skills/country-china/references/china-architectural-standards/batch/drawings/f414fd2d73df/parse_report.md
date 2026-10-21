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
    "LWPOLYLINE": 114,
    "LINE": 1270,
    "HATCH": 19,
    "CIRCLE": 10,
    "INSERT": 143,
    "ARC": 11,
    "TEXT": 133
  },
  "geometry_checksum": 175218655232.0,
  "bounds": [
    [
      -684.03,
      2071.91
    ],
    [
      9269.48,
      12817.47
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
