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
    "LINE": 5433,
    "CIRCLE": 309,
    "ARC": 1332,
    "SOLID": 10,
    "TEXT": 21
  },
  "geometry_checksum": 42159554560.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      297.0,
      210.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
