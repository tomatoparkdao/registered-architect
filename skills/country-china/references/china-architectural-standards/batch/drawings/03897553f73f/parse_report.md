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
    "LINE": 251,
    "LEADER": 10,
    "HATCH": 3,
    "INSERT": 16,
    "CIRCLE": 2,
    "LWPOLYLINE": 6,
    "ARC": 24,
    "MTEXT": 10,
    "TEXT": 6,
    "DIMENSION": 5
  },
  "geometry_checksum": 664331392.0,
  "bounds": [
    [
      -9905.66,
      907.42
    ],
    [
      1087380.75,
      196259.02
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
