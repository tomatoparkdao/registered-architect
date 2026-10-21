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
    "LINE": 553,
    "HATCH": 16,
    "INSERT": 32,
    "CIRCLE": 6,
    "LWPOLYLINE": 3,
    "ELLIPSE": 30,
    "ARC": 2,
    "TEXT": 70
  },
  "geometry_checksum": 5708058624.0,
  "bounds": [
    [
      -1059138.12,
      -57.17
    ],
    [
      754064.19,
      1031282.38
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
