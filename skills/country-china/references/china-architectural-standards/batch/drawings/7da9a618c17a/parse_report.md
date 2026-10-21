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
    "LINE": 19055,
    "LWPOLYLINE": 1288,
    "ARC": 1924,
    "CIRCLE": 596,
    "INSERT": 2016,
    "HATCH": 513,
    "POLYLINE": 12,
    "SPLINE": 5,
    "SOLID": 20,
    "MTEXT": 73,
    "TEXT": 22
  },
  "geometry_checksum": 414135342858240.0,
  "bounds": [
    [
      -85068.4,
      -224670.44
    ],
    [
      179700.27,
      336387.84
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
