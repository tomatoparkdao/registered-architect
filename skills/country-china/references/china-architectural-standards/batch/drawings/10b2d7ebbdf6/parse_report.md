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
    "CIRCLE": 5,
    "LWPOLYLINE": 8,
    "LINE": 54,
    "HATCH": 9,
    "INSERT": 6,
    "LEADER": 6,
    "TEXT": 7,
    "MTEXT": 9,
    "DIMENSION": 5
  },
  "geometry_checksum": 7839647744.0,
  "bounds": [
    [
      201276.59,
      5992.28
    ],
    [
      205431.52,
      8064.95
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
