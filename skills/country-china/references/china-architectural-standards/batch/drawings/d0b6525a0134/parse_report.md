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
    "LINE": 1068,
    "CIRCLE": 2,
    "LWPOLYLINE": 52,
    "ARC": 247,
    "INSERT": 16,
    "TEXT": 169
  },
  "geometry_checksum": 11215386624.0,
  "bounds": [
    [
      -5038.13,
      -5966.72
    ],
    [
      6588.3,
      655.95
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
