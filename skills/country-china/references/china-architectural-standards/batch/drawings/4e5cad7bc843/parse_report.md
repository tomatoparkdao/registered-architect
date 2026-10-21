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
    "LINE": 305,
    "LWPOLYLINE": 95,
    "INSERT": 40,
    "HATCH": 7,
    "ARC": 5,
    "CIRCLE": 18,
    "TEXT": 134,
    "DIMENSION": 7
  },
  "geometry_checksum": 49274347520.0,
  "bounds": [
    [
      0.0,
      -166248.62
    ],
    [
      216106.06,
      0.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
