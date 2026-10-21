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
    "LINE": 381,
    "CIRCLE": 13,
    "LWPOLYLINE": 9,
    "ARC": 48,
    "HATCH": 11,
    "INSERT": 26,
    "SOLID": 1,
    "MTEXT": 33
  },
  "geometry_checksum": 13841868800.0,
  "bounds": [
    [
      8557.2,
      3518.99
    ],
    [
      9134.64,
      3977.09
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
