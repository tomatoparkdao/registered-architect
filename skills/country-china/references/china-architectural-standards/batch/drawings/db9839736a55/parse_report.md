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
    "LINE": 142,
    "SOLID": 30,
    "CIRCLE": 1,
    "LWPOLYLINE": 1,
    "ARC": 4,
    "INSERT": 2,
    "TEXT": 44
  },
  "geometry_checksum": 65943864.0,
  "bounds": [
    [
      -45.14,
      0.0
    ],
    [
      397.01,
      286.01
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
