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
    "LEADER": 8,
    "HATCH": 8,
    "LINE": 666,
    "INSERT": 5,
    "ARC": 77,
    "LWPOLYLINE": 1,
    "TEXT": 12,
    "MTEXT": 2,
    "DIMENSION": 3
  },
  "geometry_checksum": 144782065664.0,
  "bounds": [
    [
      41583.09,
      13704.05
    ],
    [
      49988.48,
      18791.77
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
