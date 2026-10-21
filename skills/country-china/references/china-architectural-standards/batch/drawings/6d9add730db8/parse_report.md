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
    "LINE": 187,
    "CIRCLE": 2,
    "HATCH": 2,
    "ARC": 6,
    "INSERT": 2,
    "TEXT": 59
  },
  "geometry_checksum": 3338210816.0,
  "bounds": [
    [
      4004.49,
      -2375.57
    ],
    [
      16581.19,
      14290.95
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
