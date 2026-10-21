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
    "CIRCLE": 23,
    "LINE": 824,
    "INSERT": 119,
    "ARC": 64,
    "TEXT": 120
  },
  "geometry_checksum": 53429665792.0,
  "bounds": [
    [
      -13085.39,
      -1792694.88
    ],
    [
      2275814.0,
      18095.49
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
