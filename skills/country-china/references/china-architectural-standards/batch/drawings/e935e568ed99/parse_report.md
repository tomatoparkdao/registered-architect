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
    "LINE": 20,
    "INSERT": 7,
    "ARC": 2,
    "HATCH": 6,
    "CIRCLE": 2,
    "LWPOLYLINE": 6,
    "TEXT": 11,
    "MTEXT": 3,
    "DIMENSION": 9
  },
  "geometry_checksum": -6480668672.0,
  "bounds": [
    [
      -251709.44,
      -254330.94
    ],
    [
      -218280.45,
      188329.06
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
