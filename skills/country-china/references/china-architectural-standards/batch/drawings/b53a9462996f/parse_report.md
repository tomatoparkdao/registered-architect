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
    "LINE": 364,
    "CIRCLE": 19,
    "ARC": 75,
    "HATCH": 8,
    "INSERT": 4,
    "TEXT": 71
  },
  "geometry_checksum": 3469438464.0,
  "bounds": [
    [
      785.33,
      615.54
    ],
    [
      2436.0,
      2802.6
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
