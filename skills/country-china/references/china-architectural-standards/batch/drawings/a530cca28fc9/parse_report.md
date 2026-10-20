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
    "LWPOLYLINE": 463,
    "ARC": 40,
    "LINE": 86,
    "CIRCLE": 22,
    "ELLIPSE": 24
  },
  "geometry_checksum": 159703252992.0,
  "bounds": [
    [
      4395.0,
      1000.0
    ],
    [
      7995.0,
      3400.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
