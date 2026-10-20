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
    "ARC": 34,
    "CIRCLE": 12,
    "LINE": 461,
    "INSERT": 21,
    "SOLID": 18,
    "TEXT": 63
  },
  "geometry_checksum": 634543104.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      567.36,
      385.15
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
