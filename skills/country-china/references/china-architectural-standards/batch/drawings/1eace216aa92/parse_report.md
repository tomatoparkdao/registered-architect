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
    "LINE": 1703,
    "CIRCLE": 25,
    "ARC": 44,
    "INSERT": 68,
    "LWPOLYLINE": 26,
    "TEXT": 77
  },
  "geometry_checksum": 1406269184.0,
  "bounds": [
    [
      -3034.27,
      -3556.77
    ],
    [
      3343.65,
      2090.46
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
