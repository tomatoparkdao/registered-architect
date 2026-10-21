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
    "INSERT": 59,
    "LINE": 221,
    "LWPOLYLINE": 39,
    "ARC": 2,
    "HATCH": 2,
    "TEXT": 56,
    "DIMENSION": 91
  },
  "geometry_checksum": 58505437184.0,
  "bounds": [
    [
      -97294.84,
      -90894.47
    ],
    [
      47612.26,
      27283.87
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
