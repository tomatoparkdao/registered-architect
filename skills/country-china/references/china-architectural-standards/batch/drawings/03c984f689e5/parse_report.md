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
    "LINE": 346,
    "LWPOLYLINE": 4,
    "HATCH": 2,
    "ARC": 15,
    "INSERT": 6,
    "CIRCLE": 6,
    "LEADER": 1,
    "TEXT": 4,
    "MTEXT": 3,
    "DIMENSION": 5
  },
  "geometry_checksum": 173663862784.0,
  "bounds": [
    [
      280257.0,
      -2848.97
    ],
    [
      292802.16,
      -47.3
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
