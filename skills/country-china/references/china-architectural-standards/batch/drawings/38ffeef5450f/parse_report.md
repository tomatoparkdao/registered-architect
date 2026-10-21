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
    "LINE": 230,
    "HATCH": 16,
    "CIRCLE": 10,
    "LEADER": 11,
    "ARC": 11,
    "LWPOLYLINE": 27,
    "INSERT": 1,
    "TEXT": 19,
    "MTEXT": 1,
    "DIMENSION": 50
  },
  "geometry_checksum": 1329815808.0,
  "bounds": [
    [
      399.07,
      16.09
    ],
    [
      897.92,
      1172.45
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
