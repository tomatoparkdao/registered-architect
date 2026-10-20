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
    "LINE": 243,
    "LWPOLYLINE": 68,
    "CIRCLE": 18,
    "ARC": 4,
    "TEXT": 1000
  },
  "geometry_checksum": 11366635520.0,
  "bounds": [
    [
      105.7,
      -210.35
    ],
    [
      4879.58,
      3569.18
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
