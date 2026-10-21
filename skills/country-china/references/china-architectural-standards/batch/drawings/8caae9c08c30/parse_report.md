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
    "LINE": 39,
    "LWPOLYLINE": 3,
    "HATCH": 3,
    "CIRCLE": 3,
    "ARC": 2,
    "INSERT": 1,
    "TEXT": 12,
    "DIMENSION": 4
  },
  "geometry_checksum": 63303224.0,
  "bounds": [
    [
      2853.86,
      -816.97
    ],
    [
      3306.37,
      -377.13
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
