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
    "LINE": 343,
    "HATCH": 25,
    "ARC": 3,
    "CIRCLE": 4,
    "INSERT": 25,
    "LWPOLYLINE": 1,
    "TEXT": 30
  },
  "geometry_checksum": 15425812480.0,
  "bounds": [
    [
      4079.76,
      -11715.51
    ],
    [
      25558.35,
      18147.08
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
