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
    "LINE": 1736,
    "INSERT": 49,
    "HATCH": 16,
    "ARC": 808,
    "LWPOLYLINE": 32,
    "ELLIPSE": 12,
    "CIRCLE": 171,
    "TEXT": 48,
    "MTEXT": 3
  },
  "geometry_checksum": 585296510976.0,
  "bounds": [
    [
      0.33,
      314.14
    ],
    [
      27015.87,
      15242.54
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
