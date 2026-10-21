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
    "LINE": 598,
    "LWPOLYLINE": 93,
    "HATCH": 3,
    "CIRCLE": 1,
    "INSERT": 59,
    "ARC": 2,
    "TEXT": 62
  },
  "geometry_checksum": 137361219584.0,
  "bounds": [
    [
      2204.63,
      -15287.71
    ],
    [
      47530.58,
      9628.77
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
