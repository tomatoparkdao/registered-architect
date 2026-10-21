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
    "INSERT": 75,
    "LWPOLYLINE": 189,
    "LINE": 1236,
    "HATCH": 97,
    "CIRCLE": 18,
    "LEADER": 61,
    "ARC": 425,
    "TEXT": 455,
    "MTEXT": 1,
    "DIMENSION": 183
  },
  "geometry_checksum": 39250254888960.0,
  "bounds": [
    [
      -775459.31,
      0.0
    ],
    [
      889594.88,
      324723.66
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
