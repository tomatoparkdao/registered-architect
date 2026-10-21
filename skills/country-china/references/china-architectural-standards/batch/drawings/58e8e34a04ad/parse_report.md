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
    "LWPOLYLINE": 155,
    "LINE": 4135,
    "INSERT": 159,
    "ARC": 29,
    "HATCH": 11,
    "LEADER": 25,
    "CIRCLE": 25,
    "TEXT": 136
  },
  "geometry_checksum": 515059515392.0,
  "bounds": [
    [
      1400.77,
      498.18
    ],
    [
      5183.42,
      5303.89
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
