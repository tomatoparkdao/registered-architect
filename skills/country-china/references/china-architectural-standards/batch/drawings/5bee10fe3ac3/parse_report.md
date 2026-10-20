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
    "LINE": 202,
    "LWPOLYLINE": 58,
    "CIRCLE": 13,
    "ARC": 9,
    "TEXT": 1319
  },
  "geometry_checksum": 9864821760.0,
  "bounds": [
    [
      -209.18,
      -102.02
    ],
    [
      3098.41,
      3052.06
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
