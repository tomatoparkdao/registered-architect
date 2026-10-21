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
    "LINE": 303,
    "INSERT": 18,
    "HATCH": 14,
    "ARC": 189,
    "CIRCLE": 8,
    "LWPOLYLINE": 4,
    "ELLIPSE": 2,
    "TEXT": 26,
    "MTEXT": 9
  },
  "geometry_checksum": 11694059520.0,
  "bounds": [
    [
      8749.79,
      3011.18
    ],
    [
      9762.04,
      4410.03
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
