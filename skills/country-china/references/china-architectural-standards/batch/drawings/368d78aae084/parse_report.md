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
    "LWPOLYLINE": 46,
    "CIRCLE": 1,
    "LINE": 81,
    "ARC": 3,
    "INSERT": 4,
    "TEXT": 211
  },
  "geometry_checksum": 242698608.0,
  "bounds": [
    [
      42.98,
      261.44
    ],
    [
      788.9,
      1175.68
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
