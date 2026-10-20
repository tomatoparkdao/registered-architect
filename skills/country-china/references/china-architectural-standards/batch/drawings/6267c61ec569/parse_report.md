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
    "LEADER": 48,
    "LINE": 1793,
    "LWPOLYLINE": 37,
    "HATCH": 11,
    "CIRCLE": 11,
    "ARC": 18,
    "INSERT": 16,
    "TEXT": 61,
    "DIMENSION": 81
  },
  "geometry_checksum": 232854880256.0,
  "bounds": [
    [
      143.06,
      195.51
    ],
    [
      8760.37,
      11669.33
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
