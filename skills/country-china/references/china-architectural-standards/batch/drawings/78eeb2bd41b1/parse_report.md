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
    "LINE": 920,
    "CIRCLE": 27,
    "ELLIPSE": 3,
    "ARC": 39,
    "INSERT": 31,
    "LWPOLYLINE": 17,
    "TEXT": 49
  },
  "geometry_checksum": 10265520128.0,
  "bounds": [
    [
      1271.59,
      430.78
    ],
    [
      2295.06,
      1657.97
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
