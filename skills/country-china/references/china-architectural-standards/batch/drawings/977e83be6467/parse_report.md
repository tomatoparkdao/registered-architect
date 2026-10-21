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
    "LINE": 166,
    "LWPOLYLINE": 30,
    "CIRCLE": 4,
    "HATCH": 17,
    "INSERT": 11,
    "ARC": 15,
    "MTEXT": 14,
    "TEXT": 6
  },
  "geometry_checksum": 4858514432.0,
  "bounds": [
    [
      7799.51,
      4109.6
    ],
    [
      9398.57,
      5331.44
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
