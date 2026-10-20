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
    "ARC": 36,
    "SPLINE": 36,
    "LINE": 174,
    "LWPOLYLINE": 6,
    "CIRCLE": 4,
    "DIMENSION": 4
  },
  "geometry_checksum": 310969856.0,
  "bounds": [
    [
      100.5,
      1087.56
    ],
    [
      376.59,
      1575.56
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
