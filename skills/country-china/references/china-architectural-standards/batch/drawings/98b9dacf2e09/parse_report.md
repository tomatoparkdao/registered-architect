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
    "LWPOLYLINE": 296,
    "CIRCLE": 13,
    "LINE": 1518,
    "ARC": 47,
    "HATCH": 36,
    "INSERT": 203,
    "TEXT": 157
  },
  "geometry_checksum": 345289818112.0,
  "bounds": [
    [
      3695.09,
      2065.5
    ],
    [
      11905.49,
      11825.74
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
