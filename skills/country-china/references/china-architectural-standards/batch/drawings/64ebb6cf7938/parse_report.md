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
    "ARC": 18,
    "CIRCLE": 10,
    "SOLID": 27,
    "INSERT": 2,
    "LWPOLYLINE": 1,
    "TEXT": 36
  },
  "geometry_checksum": 36376288.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      414.41,
      276.6
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
