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
    "LWPOLYLINE": 8,
    "HATCH": 2,
    "LINE": 44,
    "INSERT": 5,
    "TEXT": 12,
    "DIMENSION": 8
  },
  "geometry_checksum": 690159296.0,
  "bounds": [
    [
      3010.52,
      18988.49
    ],
    [
      4924.2,
      21522.62
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
