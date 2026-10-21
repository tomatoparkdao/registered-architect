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
    "LINE": 305,
    "ARC": 13,
    "LWPOLYLINE": 21,
    "LEADER": 11,
    "HATCH": 5,
    "CIRCLE": 2,
    "MTEXT": 10,
    "TEXT": 149,
    "DIMENSION": 24
  },
  "geometry_checksum": -483256827904.0,
  "bounds": [
    [
      -352456.62,
      -46729.49
    ],
    [
      -350356.62,
      -45244.49
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
