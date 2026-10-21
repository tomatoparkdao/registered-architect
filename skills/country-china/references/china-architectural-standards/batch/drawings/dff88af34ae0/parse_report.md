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
    "LINE": 219,
    "CIRCLE": 30,
    "ARC": 1345,
    "INSERT": 20,
    "TEXT": 10
  },
  "geometry_checksum": 8878773248.0,
  "bounds": [
    [
      1312.3,
      -714.13
    ],
    [
      2750.36,
      3585.03
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
