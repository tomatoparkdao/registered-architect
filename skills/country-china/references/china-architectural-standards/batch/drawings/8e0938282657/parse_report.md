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
    "INSERT": 7,
    "LINE": 564,
    "ARC": 60,
    "CIRCLE": 13,
    "LWPOLYLINE": 3,
    "SOLID": 93,
    "TEXT": 123
  },
  "geometry_checksum": 2202245632.0,
  "bounds": [
    [
      -224.2,
      -124.35
    ],
    [
      814.88,
      582.19
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
