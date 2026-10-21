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
    "LINE": 477,
    "CIRCLE": 11,
    "INSERT": 24,
    "LWPOLYLINE": 51,
    "ARC": 8,
    "HATCH": 7,
    "TEXT": 41,
    "MTEXT": 4,
    "DIMENSION": 54
  },
  "geometry_checksum": 101034647552.0,
  "bounds": [
    [
      -24357.31,
      -228.94
    ],
    [
      31452.25,
      25564.2
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
