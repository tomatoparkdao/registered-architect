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
    "ARC": 75,
    "LINE": 208,
    "CIRCLE": 3,
    "SOLID": 58,
    "INSERT": 5,
    "LWPOLYLINE": 2,
    "TEXT": 57
  },
  "geometry_checksum": 253854896.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      389.37,
      290.16
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
