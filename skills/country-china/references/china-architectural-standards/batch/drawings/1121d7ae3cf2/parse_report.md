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
    "LWPOLYLINE": 679,
    "LINE": 1877,
    "INSERT": 27,
    "ARC": 62,
    "CIRCLE": 8,
    "TEXT": 399,
    "MTEXT": 13,
    "DIMENSION": 45
  },
  "geometry_checksum": 8159615778816.0,
  "bounds": [
    [
      -39642.46,
      105579.15
    ],
    [
      78982.8,
      193849.5
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
