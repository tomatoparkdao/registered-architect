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
    "LINE": 382,
    "CIRCLE": 4,
    "ELLIPSE": 12,
    "INSERT": 22,
    "HATCH": 7,
    "LWPOLYLINE": 6,
    "TEXT": 46
  },
  "geometry_checksum": 9668292608.0,
  "bounds": [
    [
      -853301.5,
      -3006742.25
    ],
    [
      5030259.5,
      1716334.75
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
