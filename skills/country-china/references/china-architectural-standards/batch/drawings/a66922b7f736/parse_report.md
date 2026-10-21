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
    "LINE": 1040,
    "INSERT": 33,
    "LWPOLYLINE": 197,
    "CIRCLE": 10,
    "ARC": 8,
    "HATCH": 12,
    "TEXT": 93,
    "DIMENSION": 134
  },
  "geometry_checksum": 194286256128.0,
  "bounds": [
    [
      -43788.82,
      -127146.48
    ],
    [
      18041.31,
      18780.87
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
