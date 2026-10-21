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
    "LWPOLYLINE": 10,
    "LINE": 33,
    "CIRCLE": 2,
    "HATCH": 1,
    "LEADER": 1,
    "MTEXT": 1,
    "TEXT": 17
  },
  "geometry_checksum": 15415656448.0,
  "bounds": [
    [
      354565.91,
      283854.38
    ],
    [
      369355.88,
      287986.88
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
