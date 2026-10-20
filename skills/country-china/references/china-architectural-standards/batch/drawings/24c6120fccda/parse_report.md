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
    "LINE": 262,
    "LWPOLYLINE": 73,
    "INSERT": 8,
    "ARC": 4,
    "CIRCLE": 2,
    "TEXT": 20,
    "DIMENSION": 31
  },
  "geometry_checksum": 19067478016.0,
  "bounds": [
    [
      -27083.56,
      -1258.92
    ],
    [
      28145.73,
      15156.65
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
