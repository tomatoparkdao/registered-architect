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
    "LINE": 575,
    "LWPOLYLINE": 22,
    "CIRCLE": 4,
    "ARC": 5,
    "INSERT": 8,
    "TEXT": 48
  },
  "geometry_checksum": 890337152.0,
  "bounds": [
    [
      123.86,
      95.83
    ],
    [
      214.97,
      282.91
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
