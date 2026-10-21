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
    "LINE": 4237,
    "ARC": 1651,
    "SPLINE": 48,
    "CIRCLE": 28,
    "ELLIPSE": 408,
    "INSERT": 91,
    "LWPOLYLINE": 5,
    "TEXT": 75
  },
  "geometry_checksum": 475787689984.0,
  "bounds": [
    [
      -3250.12,
      -3528.23
    ],
    [
      9578.71,
      5339.82
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
