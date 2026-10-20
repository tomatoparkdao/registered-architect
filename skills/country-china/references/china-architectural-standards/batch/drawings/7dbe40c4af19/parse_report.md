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
    "LINE": 53,
    "SOLID": 7,
    "CIRCLE": 1,
    "LWPOLYLINE": 3,
    "ARC": 3,
    "INSERT": 2,
    "TEXT": 23
  },
  "geometry_checksum": 9248456.0,
  "bounds": [
    [
      -115.06,
      -145.79
    ],
    [
      203.88,
      291.16
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
