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
    "CIRCLE": 5,
    "LINE": 406,
    "ARC": 47,
    "LWPOLYLINE": 2,
    "INSERT": 11,
    "SOLID": 71,
    "TEXT": 84
  },
  "geometry_checksum": 733640192.0,
  "bounds": [
    [
      0.0,
      -35.52
    ],
    [
      565.98,
      409.46
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
