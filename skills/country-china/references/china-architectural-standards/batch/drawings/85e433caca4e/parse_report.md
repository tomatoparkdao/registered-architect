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
    "LINE": 968,
    "ARC": 23,
    "INSERT": 34,
    "LWPOLYLINE": 73,
    "HATCH": 5,
    "CIRCLE": 4,
    "TEXT": 43,
    "DIMENSION": 371
  },
  "geometry_checksum": -98124087296.0,
  "bounds": [
    [
      -47358.17,
      -9368.49
    ],
    [
      15456.63,
      31982.5
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
