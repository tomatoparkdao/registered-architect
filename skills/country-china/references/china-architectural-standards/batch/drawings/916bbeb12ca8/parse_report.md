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
    "LEADER": 25,
    "ARC": 29,
    "LWPOLYLINE": 154,
    "LINE": 3743,
    "CIRCLE": 25,
    "HATCH": 11,
    "INSERT": 40,
    "TEXT": 39,
    "DIMENSION": 98
  },
  "geometry_checksum": 410007076864.0,
  "bounds": [
    [
      0.8,
      165.94
    ],
    [
      3494.44,
      4676.17
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
