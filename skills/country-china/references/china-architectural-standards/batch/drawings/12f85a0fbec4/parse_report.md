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
    "LINE": 194,
    "CIRCLE": 1,
    "HATCH": 8,
    "LEADER": 13,
    "INSERT": 18,
    "ARC": 23,
    "LWPOLYLINE": 9,
    "TEXT": 5,
    "MTEXT": 13,
    "DIMENSION": 6
  },
  "geometry_checksum": 19864360960.0,
  "bounds": [
    [
      39101.09,
      4091.83
    ],
    [
      44447.32,
      10050.5
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
