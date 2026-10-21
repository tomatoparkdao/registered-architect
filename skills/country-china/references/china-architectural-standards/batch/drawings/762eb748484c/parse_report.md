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
    "LINE": 43,
    "CIRCLE": 2,
    "HATCH": 4,
    "LWPOLYLINE": 7,
    "INSERT": 1,
    "TEXT": 12,
    "DIMENSION": 5
  },
  "geometry_checksum": 276715232.0,
  "bounds": [
    [
      9653.93,
      733.67
    ],
    [
      11858.79,
      3157.04
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
