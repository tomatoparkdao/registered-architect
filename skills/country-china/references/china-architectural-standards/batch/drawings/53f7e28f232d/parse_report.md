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
    "LINE": 359,
    "INSERT": 48,
    "LEADER": 9,
    "LWPOLYLINE": 35,
    "HATCH": 4,
    "CIRCLE": 5,
    "TEXT": 19,
    "DIMENSION": 29
  },
  "geometry_checksum": 12551734272.0,
  "bounds": [
    [
      -391.34,
      5073.21
    ],
    [
      5511.7,
      8615.92
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
