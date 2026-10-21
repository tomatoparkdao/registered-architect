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
    "CIRCLE": 20,
    "LINE": 987,
    "INSERT": 90,
    "LWPOLYLINE": 19,
    "HATCH": 18,
    "ARC": 116,
    "TEXT": 136
  },
  "geometry_checksum": 2588294512640.0,
  "bounds": [
    [
      77146.03,
      232648.17
    ],
    [
      133139.44,
      305661.97
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
