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
    "LINE": 1615,
    "LWPOLYLINE": 23,
    "INSERT": 3,
    "HATCH": 1,
    "TEXT": 23,
    "DIMENSION": 7
  },
  "geometry_checksum": 23063891968.0,
  "bounds": [
    [
      -1736.0,
      317.6
    ],
    [
      1980.0,
      2846.48
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
