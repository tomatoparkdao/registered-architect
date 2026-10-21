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
    "LINE": 158,
    "ARC": 14,
    "CIRCLE": 2,
    "HATCH": 11,
    "LWPOLYLINE": 20,
    "INSERT": 12,
    "TEXT": 23,
    "MTEXT": 5
  },
  "geometry_checksum": 89451593728.0,
  "bounds": [
    [
      112800.78,
      39028.6
    ],
    [
      113150.7,
      39674.43
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
