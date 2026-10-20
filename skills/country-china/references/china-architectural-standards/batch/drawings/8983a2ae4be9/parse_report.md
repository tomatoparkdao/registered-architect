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
    "LWPOLYLINE": 113,
    "LINE": 887,
    "INSERT": 21,
    "CIRCLE": 63,
    "TEXT": 127,
    "DIMENSION": 132
  },
  "geometry_checksum": 441212534784.0,
  "bounds": [
    [
      -411510.19,
      -18169.57
    ],
    [
      65047.47,
      50306.01
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
