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
    "LINE": 1424,
    "ARC": 112,
    "INSERT": 84,
    "LEADER": 33,
    "LWPOLYLINE": 57,
    "HATCH": 24,
    "CIRCLE": 8,
    "TEXT": 92,
    "MTEXT": 1
  },
  "geometry_checksum": 161966653440.0,
  "bounds": [
    [
      1008.09,
      279.13
    ],
    [
      10230.72,
      12092.65
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
