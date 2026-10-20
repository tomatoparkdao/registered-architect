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
    "LINE": 158,
    "CIRCLE": 1,
    "SOLID": 35,
    "ARC": 9,
    "INSERT": 3,
    "LWPOLYLINE": 1,
    "TEXT": 48
  },
  "geometry_checksum": 91279360.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      398.19,
      289.26
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
