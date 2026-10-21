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
    "LINE": 185,
    "LWPOLYLINE": 30,
    "INSERT": 2,
    "HATCH": 4,
    "ARC": 14,
    "TEXT": 99,
    "DIMENSION": 11
  },
  "geometry_checksum": -7948382208.0,
  "bounds": [
    [
      -13590.06,
      -36014.95
    ],
    [
      3682.34,
      -8654.95
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
