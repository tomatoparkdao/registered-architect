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
    "CIRCLE": 5,
    "LWPOLYLINE": 13,
    "HATCH": 23,
    "LINE": 1350,
    "ARC": 78,
    "INSERT": 16,
    "ELLIPSE": 1,
    "MTEXT": 15,
    "TEXT": 13
  },
  "geometry_checksum": 2412851757056.0,
  "bounds": [
    [
      7032.8,
      19965.02
    ],
    [
      234575.3,
      260752.05
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
