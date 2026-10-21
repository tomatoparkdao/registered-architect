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
    "LINE": 470,
    "CIRCLE": 8,
    "LWPOLYLINE": 25,
    "LEADER": 23,
    "HATCH": 12,
    "ARC": 3,
    "ELLIPSE": 1,
    "INSERT": 1,
    "TEXT": 308,
    "MTEXT": 24,
    "DIMENSION": 35
  },
  "geometry_checksum": -1154376007680.0,
  "bounds": [
    [
      -352771.66,
      -48446.8
    ],
    [
      -347801.88,
      -45244.49
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
