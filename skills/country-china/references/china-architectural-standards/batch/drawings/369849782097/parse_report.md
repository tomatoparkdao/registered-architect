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
    "LINE": 68,
    "CIRCLE": 7,
    "SOLID": 30,
    "INSERT": 2,
    "LWPOLYLINE": 1,
    "ARC": 19,
    "TEXT": 37
  },
  "geometry_checksum": 40181444.0,
  "bounds": [
    [
      -594.0,
      0.0
    ],
    [
      395.2,
      287.9
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
