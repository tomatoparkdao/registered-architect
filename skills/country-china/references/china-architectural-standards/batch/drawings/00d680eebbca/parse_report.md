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
    "LWPOLYLINE": 125,
    "LINE": 2011,
    "ARC": 93,
    "LEADER": 43,
    "CIRCLE": 10,
    "HATCH": 10,
    "INSERT": 97,
    "TEXT": 120
  },
  "geometry_checksum": 356900077568.0,
  "bounds": [
    [
      -20905.95,
      1073.55
    ],
    [
      28457.76,
      12793.86
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
