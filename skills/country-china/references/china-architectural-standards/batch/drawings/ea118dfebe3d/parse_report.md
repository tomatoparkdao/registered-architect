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
    "LWPOLYLINE": 88,
    "LINE": 10979,
    "HATCH": 24,
    "CIRCLE": 12,
    "ARC": 33,
    "LEADER": 29,
    "INSERT": 88,
    "TEXT": 109
  },
  "geometry_checksum": 4928088047616.0,
  "bounds": [
    [
      -14146.68,
      427.42
    ],
    [
      242994.83,
      10275.2
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
