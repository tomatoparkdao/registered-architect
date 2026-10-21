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
    "LINE": 434,
    "HATCH": 38,
    "CIRCLE": 5,
    "ELLIPSE": 6,
    "INSERT": 22,
    "TEXT": 66
  },
  "geometry_checksum": 5438358528.0,
  "bounds": [
    [
      -953635.56,
      -171893.73
    ],
    [
      1343937.38,
      641682.44
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
