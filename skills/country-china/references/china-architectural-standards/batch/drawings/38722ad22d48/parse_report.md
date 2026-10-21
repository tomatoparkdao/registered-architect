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
    "LINE": 354,
    "LWPOLYLINE": 44,
    "ARC": 5,
    "CIRCLE": 10,
    "TEXT": 46,
    "DIMENSION": 21
  },
  "geometry_checksum": 1947456000.0,
  "bounds": [
    [
      -2687.0,
      609.0
    ],
    [
      4067.17,
      2135.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
