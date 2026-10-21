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
    "LINE": 563,
    "CIRCLE": 4,
    "LWPOLYLINE": 47,
    "HATCH": 12,
    "ARC": 24,
    "INSERT": 10,
    "TEXT": 21,
    "MTEXT": 5
  },
  "geometry_checksum": 17672163328.0,
  "bounds": [
    [
      3807.89,
      1633.81
    ],
    [
      4722.59,
      2966.83
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
