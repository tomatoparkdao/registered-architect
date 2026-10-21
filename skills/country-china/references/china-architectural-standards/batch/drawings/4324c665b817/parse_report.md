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
    "HATCH": 18,
    "LINE": 784,
    "ARC": 22,
    "CIRCLE": 24,
    "INSERT": 95,
    "LWPOLYLINE": 5,
    "TEXT": 103
  },
  "geometry_checksum": 72782643200.0,
  "bounds": [
    [
      1284.92,
      145.62
    ],
    [
      18733.83,
      16274.45
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
