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
    "ARC": 71,
    "LINE": 216,
    "INSERT": 6,
    "CIRCLE": 3,
    "SOLID": 55,
    "LWPOLYLINE": 3,
    "TEXT": 64
  },
  "geometry_checksum": 233203328.0,
  "bounds": [
    [
      -2.33,
      -1.52
    ],
    [
      397.44,
      290.05
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
