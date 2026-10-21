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
    "LWPOLYLINE": 82,
    "LINE": 2346,
    "CIRCLE": 23,
    "ARC": 45,
    "HATCH": 96,
    "ELLIPSE": 6,
    "INSERT": 9,
    "TEXT": 238,
    "MTEXT": 5,
    "DIMENSION": 3
  },
  "geometry_checksum": 6396924919808.0,
  "bounds": [
    [
      99635.13,
      -80907.75
    ],
    [
      566576.81,
      132016.7
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
