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
    "LINE": 1989,
    "LEADER": 18,
    "LWPOLYLINE": 232,
    "CIRCLE": 14,
    "ARC": 49,
    "INSERT": 4,
    "HATCH": 20,
    "MTEXT": 29,
    "TEXT": 152,
    "DIMENSION": 113
  },
  "geometry_checksum": 4716325502976.0,
  "bounds": [
    [
      154704.44,
      -26293.64
    ],
    [
      174258.62,
      -17383.64
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
