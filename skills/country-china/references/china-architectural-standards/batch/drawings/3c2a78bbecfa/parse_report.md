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
    "LINE": 1438,
    "LWPOLYLINE": 62,
    "ARC": 56,
    "CIRCLE": 63,
    "ELLIPSE": 2,
    "HATCH": 70,
    "TEXT": 128,
    "DIMENSION": 300
  },
  "geometry_checksum": 1708982009856.0,
  "bounds": [
    [
      0.0,
      -4831.14
    ],
    [
      81967.4,
      28703.96
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
