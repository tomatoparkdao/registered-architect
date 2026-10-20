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
    "HATCH": 11,
    "LINE": 1787,
    "LWPOLYLINE": 49,
    "CIRCLE": 6,
    "LEADER": 51,
    "INSERT": 18,
    "ARC": 1,
    "TEXT": 64,
    "DIMENSION": 45
  },
  "geometry_checksum": 233097822208.0,
  "bounds": [
    [
      178.32,
      145.46
    ],
    [
      8844.84,
      11675.38
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
