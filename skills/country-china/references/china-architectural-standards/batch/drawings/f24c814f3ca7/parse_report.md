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
    "LEADER": 20,
    "LWPOLYLINE": 174,
    "LINE": 97,
    "CIRCLE": 28,
    "HATCH": 3,
    "ARC": 32,
    "TEXT": 28,
    "DIMENSION": 60
  },
  "geometry_checksum": 15340359680.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      5442.2,
      7024.63
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
