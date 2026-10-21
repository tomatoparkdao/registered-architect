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
    "INSERT": 75,
    "LINE": 603,
    "HATCH": 11,
    "ARC": 114,
    "LWPOLYLINE": 14,
    "ELLIPSE": 16,
    "CIRCLE": 11,
    "LEADER": 2,
    "MTEXT": 20,
    "TEXT": 45
  },
  "geometry_checksum": 6878754304.0,
  "bounds": [
    [
      -1966.12,
      545.69
    ],
    [
      1961.64,
      1197.19
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
