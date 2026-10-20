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
    "LEADER": 22,
    "LWPOLYLINE": 171,
    "LINE": 334,
    "ARC": 27,
    "HATCH": 21,
    "CIRCLE": 7,
    "TEXT": 47,
    "DIMENSION": 24
  },
  "geometry_checksum": 19084249088.0,
  "bounds": [
    [
      100.78,
      270.67
    ],
    [
      5331.12,
      6926.03
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
