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
    "LINE": 137,
    "CIRCLE": 3,
    "LWPOLYLINE": 16,
    "SOLID": 48,
    "ARC": 4,
    "INSERT": 2,
    "TEXT": 55
  },
  "geometry_checksum": 132759872.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      391.55,
      289.43
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
