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
    "LINE": 170,
    "ARC": 4,
    "INSERT": 3,
    "LWPOLYLINE": 5,
    "CIRCLE": 2,
    "TEXT": 15,
    "DIMENSION": 43
  },
  "geometry_checksum": 2666758144.0,
  "bounds": [
    [
      3468.49,
      -640.0
    ],
    [
      10127.81,
      3010.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
