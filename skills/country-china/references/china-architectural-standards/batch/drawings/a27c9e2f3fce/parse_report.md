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
    "LINE": 122,
    "HATCH": 3,
    "ARC": 32,
    "LWPOLYLINE": 12,
    "INSERT": 6,
    "TEXT": 13,
    "DIMENSION": 4
  },
  "geometry_checksum": 2807250176.0,
  "bounds": [
    [
      8594.19,
      9937.29
    ],
    [
      9465.88,
      10311.83
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
