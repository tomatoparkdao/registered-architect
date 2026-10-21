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
    "LINE": 247,
    "HATCH": 34,
    "CIRCLE": 10,
    "ARC": 4,
    "TEXT": 42
  },
  "geometry_checksum": 14009157632.0,
  "bounds": [
    [
      2759.46,
      481.29
    ],
    [
      20811.9,
      14857.64
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
