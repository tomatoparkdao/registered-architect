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
    "LINE": 605,
    "HATCH": 14,
    "CIRCLE": 2,
    "LWPOLYLINE": 1,
    "ARC": 3,
    "INSERT": 38,
    "MTEXT": 8,
    "TEXT": 41
  },
  "geometry_checksum": 111918055424.0,
  "bounds": [
    [
      15909.89,
      1647.75
    ],
    [
      28850.6,
      35391.3
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
