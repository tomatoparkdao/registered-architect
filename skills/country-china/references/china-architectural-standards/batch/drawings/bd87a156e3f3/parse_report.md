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
    "LINE": 253,
    "ARC": 13,
    "HATCH": 1,
    "SOLID": 1,
    "INSERT": 38,
    "CIRCLE": 4,
    "TEXT": 40
  },
  "geometry_checksum": -58670206976.0,
  "bounds": [
    [
      -159880.73,
      -15594.05
    ],
    [
      -152825.23,
      6243.24
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
