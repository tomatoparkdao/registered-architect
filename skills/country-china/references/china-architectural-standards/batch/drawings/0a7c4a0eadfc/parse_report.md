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
    "LINE": 226,
    "HATCH": 9,
    "ARC": 37,
    "LWPOLYLINE": 26,
    "ELLIPSE": 16,
    "POLYLINE": 2,
    "INSERT": 3,
    "LEADER": 11,
    "TEXT": 17,
    "DIMENSION": 3
  },
  "geometry_checksum": 87190208512.0,
  "bounds": [
    [
      143186.02,
      -26976.02
    ],
    [
      1868327.12,
      1385064.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
