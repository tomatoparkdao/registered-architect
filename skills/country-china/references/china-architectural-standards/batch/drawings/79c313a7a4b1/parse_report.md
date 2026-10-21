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
    "LWPOLYLINE": 65,
    "LINE": 289,
    "ARC": 1,
    "HATCH": 3,
    "CIRCLE": 12,
    "TEXT": 27,
    "DIMENSION": 30
  },
  "geometry_checksum": 158523129856.0,
  "bounds": [
    [
      200888.91,
      -40065.63
    ],
    [
      215624.45,
      -3529.69
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
