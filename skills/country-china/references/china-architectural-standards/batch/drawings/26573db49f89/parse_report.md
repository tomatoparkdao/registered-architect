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
    "LINE": 85,
    "LWPOLYLINE": 44,
    "CIRCLE": 1,
    "ARC": 3,
    "INSERT": 4,
    "TEXT": 389
  },
  "geometry_checksum": 680627968.0,
  "bounds": [
    [
      -77.33,
      372.44
    ],
    [
      1624.18,
      2360.75
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
