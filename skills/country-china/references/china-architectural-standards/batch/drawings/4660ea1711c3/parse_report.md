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
    "SOLID": 30,
    "LINE": 150,
    "INSERT": 5,
    "CIRCLE": 6,
    "LWPOLYLINE": 3,
    "ARC": 11,
    "TEXT": 51
  },
  "geometry_checksum": 84941184.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      394.85,
      289.07
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
