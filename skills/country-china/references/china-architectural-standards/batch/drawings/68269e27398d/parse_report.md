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
    "LINE": 14,
    "LWPOLYLINE": 1,
    "ARC": 1,
    "HATCH": 4,
    "LEADER": 3,
    "TEXT": 2,
    "MTEXT": 5,
    "DIMENSION": 1
  },
  "geometry_checksum": 462452352.0,
  "bounds": [
    [
      82958.6,
      8484.73
    ],
    [
      83104.58,
      8626.35
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
