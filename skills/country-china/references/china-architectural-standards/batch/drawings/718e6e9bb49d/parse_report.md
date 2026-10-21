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
    "CIRCLE": 5,
    "LINE": 595,
    "INSERT": 44,
    "HATCH": 42,
    "ELLIPSE": 15,
    "TEXT": 87
  },
  "geometry_checksum": 8919350272.0,
  "bounds": [
    [
      -1059487.0,
      -190120.16
    ],
    [
      1493192.38,
      711738.25
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
