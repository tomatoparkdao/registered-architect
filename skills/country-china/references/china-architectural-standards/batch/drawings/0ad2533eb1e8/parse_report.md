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
    "LINE": 776,
    "LEADER": 5,
    "LWPOLYLINE": 2,
    "ARC": 62,
    "CIRCLE": 12,
    "HATCH": 18,
    "SOLID": 6,
    "INSERT": 9,
    "TEXT": 7,
    "MTEXT": 5
  },
  "geometry_checksum": 43779633152.0,
  "bounds": [
    [
      2140.3,
      2411.65
    ],
    [
      4972.82,
      6573.45
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
