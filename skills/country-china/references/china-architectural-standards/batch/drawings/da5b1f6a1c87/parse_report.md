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
    "LINE": 624,
    "LWPOLYLINE": 114,
    "HATCH": 15,
    "INSERT": 19,
    "ARC": 46,
    "ELLIPSE": 1,
    "CIRCLE": 8,
    "TEXT": 29,
    "MTEXT": 9,
    "DIMENSION": 1
  },
  "geometry_checksum": 12618129408.0,
  "bounds": [
    [
      -2664.76,
      858.61
    ],
    [
      3128.94,
      2077.68
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
