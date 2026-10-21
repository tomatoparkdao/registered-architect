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
    "LEADER": 5,
    "HATCH": 9,
    "LINE": 57,
    "LWPOLYLINE": 8,
    "CIRCLE": 2,
    "MTEXT": 5,
    "TEXT": 3,
    "DIMENSION": 7
  },
  "geometry_checksum": 1891339520.0,
  "bounds": [
    [
      80585.37,
      -49198.77
    ],
    [
      84752.1,
      -46882.93
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
