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
    "LINE": 67,
    "INSERT": 2,
    "HATCH": 10,
    "LEADER": 10,
    "ARC": 4,
    "LWPOLYLINE": 10,
    "CIRCLE": 1,
    "TEXT": 13,
    "MTEXT": 5,
    "DIMENSION": 3
  },
  "geometry_checksum": 11635275776.0,
  "bounds": [
    [
      182012.55,
      -7719.95
    ],
    [
      184135.42,
      -6565.32
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
