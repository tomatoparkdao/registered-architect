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
    "LINE": 142,
    "LWPOLYLINE": 52,
    "CIRCLE": 2,
    "ARC": 80,
    "TEXT": 27
  },
  "geometry_checksum": 133018184.0,
  "bounds": [
    [
      27.85,
      288.69
    ],
    [
      135.55,
      361.35
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
