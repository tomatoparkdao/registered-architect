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
    "LINE": 413,
    "CIRCLE": 64,
    "LWPOLYLINE": 4,
    "ARC": 35,
    "ELLIPSE": 3,
    "INSERT": 6,
    "TEXT": 52,
    "MTEXT": 3
  },
  "geometry_checksum": 14349449216.0,
  "bounds": [
    [
      2407.95,
      7073.72
    ],
    [
      8584.23,
      9278.63
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
