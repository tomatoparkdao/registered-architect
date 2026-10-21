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
    "LWPOLYLINE": 22,
    "SOLID": 8,
    "LINE": 432,
    "HATCH": 6,
    "INSERT": 56,
    "CIRCLE": 12,
    "TEXT": 113
  },
  "geometry_checksum": 55311949824.0,
  "bounds": [
    [
      732.99,
      370.52
    ],
    [
      18807.91,
      53518.48
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
