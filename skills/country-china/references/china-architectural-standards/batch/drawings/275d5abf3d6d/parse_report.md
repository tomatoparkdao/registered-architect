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
    "LINE": 254,
    "LWPOLYLINE": 8,
    "INSERT": 2,
    "HATCH": 6,
    "MTEXT": 6,
    "TEXT": 2,
    "DIMENSION": 8
  },
  "geometry_checksum": 37862895616.0,
  "bounds": [
    [
      -85528.82,
      181877.2
    ],
    [
      -74785.98,
      192580.06
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
