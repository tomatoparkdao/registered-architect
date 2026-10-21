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
    "LINE": 71,
    "LWPOLYLINE": 8,
    "INSERT": 6,
    "HATCH": 4,
    "CIRCLE": 3,
    "TEXT": 13,
    "DIMENSION": 12
  },
  "geometry_checksum": 805214464.0,
  "bounds": [
    [
      9592.21,
      676.01
    ],
    [
      12173.26,
      3575.4
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
