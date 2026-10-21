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
    "LINE": 339,
    "HATCH": 18,
    "ARC": 27,
    "INSERT": 23,
    "CIRCLE": 8,
    "ELLIPSE": 3,
    "LWPOLYLINE": 2,
    "TEXT": 61
  },
  "geometry_checksum": 7905438720.0,
  "bounds": [
    [
      -207371.66,
      -186752.52
    ],
    [
      1497791.88,
      610882.62
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
