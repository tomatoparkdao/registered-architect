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
    "ARC": 17,
    "LEADER": 14,
    "LINE": 247,
    "CIRCLE": 16,
    "INSERT": 1,
    "HATCH": 12,
    "MTEXT": 30,
    "DIMENSION": 41
  },
  "geometry_checksum": 54611599360.0,
  "bounds": [
    [
      114865.49,
      -36983.56
    ],
    [
      117196.9,
      -34493.2
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
