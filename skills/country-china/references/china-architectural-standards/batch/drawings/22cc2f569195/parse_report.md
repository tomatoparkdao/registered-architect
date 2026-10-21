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
    "LINE": 823,
    "CIRCLE": 29,
    "HATCH": 38,
    "LWPOLYLINE": 295,
    "INSERT": 11,
    "TEXT": 49,
    "DIMENSION": 168
  },
  "geometry_checksum": -3798281486336.0,
  "bounds": [
    [
      -699170.44,
      -32800.0
    ],
    [
      -136520.44,
      187662.55
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
