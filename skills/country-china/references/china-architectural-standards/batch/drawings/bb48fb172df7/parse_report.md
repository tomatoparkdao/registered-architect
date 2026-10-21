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
    "LINE": 454,
    "ARC": 146,
    "CIRCLE": 4,
    "INSERT": 79,
    "TEXT": 73
  },
  "geometry_checksum": 11302756352.0,
  "bounds": [
    [
      -27763.42,
      15384.07
    ],
    [
      -12581.43,
      33169.37
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
