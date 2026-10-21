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
    "LINE": 539,
    "ARC": 36,
    "CIRCLE": 12,
    "HATCH": 4,
    "SPLINE": 7,
    "INSERT": 103,
    "TEXT": 119
  },
  "geometry_checksum": 48730324992.0,
  "bounds": [
    [
      -6816.8,
      18103.88
    ],
    [
      5233.79,
      34563.79
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
