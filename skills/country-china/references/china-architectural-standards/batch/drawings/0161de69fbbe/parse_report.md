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
    "LINE": 240,
    "SOLID": 52,
    "ARC": 48,
    "CIRCLE": 3,
    "INSERT": 7,
    "LWPOLYLINE": 2,
    "TEXT": 70
  },
  "geometry_checksum": 247819664.0,
  "bounds": [
    [
      -3.18,
      0.0
    ],
    [
      396.42,
      289.82
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
