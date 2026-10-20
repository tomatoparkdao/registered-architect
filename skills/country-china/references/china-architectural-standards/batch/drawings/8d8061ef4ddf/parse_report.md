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
    "LINE": 30,
    "LWPOLYLINE": 7,
    "HATCH": 2,
    "CIRCLE": 2,
    "ELLIPSE": 1
  },
  "geometry_checksum": 14340949.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      920.0,
      2100.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
