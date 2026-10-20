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
    "LINE": 178,
    "CIRCLE": 3,
    "ARC": 10,
    "LWPOLYLINE": 3,
    "SOLID": 42,
    "INSERT": 1,
    "TEXT": 46
  },
  "geometry_checksum": 148651232.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      398.08,
      289.7
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
