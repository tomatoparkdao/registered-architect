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
    "ARC": 74,
    "LINE": 188,
    "SPLINE": 4,
    "ELLIPSE": 4,
    "LWPOLYLINE": 78,
    "CIRCLE": 40
  },
  "geometry_checksum": 1611663616.0,
  "bounds": [
    [
      -362.59,
      0.0
    ],
    [
      1242.59,
      2344.79
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
