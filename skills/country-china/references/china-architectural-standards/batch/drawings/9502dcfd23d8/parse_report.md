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
    "LWPOLYLINE": 38,
    "LINE": 791,
    "HATCH": 27,
    "ARC": 95,
    "CIRCLE": 23,
    "INSERT": 52,
    "TEXT": 1,
    "MTEXT": 37
  },
  "geometry_checksum": 38571470848.0,
  "bounds": [
    [
      4267.97,
      2756.46
    ],
    [
      4392.95,
      2973.1
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
