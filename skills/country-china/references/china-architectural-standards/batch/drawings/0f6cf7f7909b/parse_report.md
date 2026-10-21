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
    "ARC": 1067,
    "INSERT": 6,
    "LINE": 2049,
    "LWPOLYLINE": 851,
    "SOLID": 1,
    "POLYLINE": 80,
    "CIRCLE": 78,
    "ELLIPSE": 100,
    "HATCH": 4,
    "TEXT": 59,
    "DIMENSION": 249
  },
  "geometry_checksum": -81593696256.0,
  "bounds": [
    [
      -279.53,
      -30.55
    ],
    [
      -266.61,
      -18.03
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
