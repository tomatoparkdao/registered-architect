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
    "INSERT": 11,
    "ARC": 102,
    "LINE": 493,
    "CIRCLE": 10,
    "LWPOLYLINE": 5,
    "SOLID": 77,
    "TEXT": 105
  },
  "geometry_checksum": 1751214848.0,
  "bounds": [
    [
      -142.85,
      -231.99
    ],
    [
      813.69,
      582.19
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
