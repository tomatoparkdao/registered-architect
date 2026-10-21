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
    "LWPOLYLINE": 35,
    "LINE": 507,
    "HATCH": 18,
    "INSERT": 75,
    "CIRCLE": 5,
    "ARC": 1,
    "TEXT": 81
  },
  "geometry_checksum": 5534151680.0,
  "bounds": [
    [
      394.28,
      -2630.33
    ],
    [
      7299.71,
      3259.77
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
