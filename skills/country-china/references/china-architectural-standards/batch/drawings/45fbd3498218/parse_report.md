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
    "LINE": 1153,
    "ARC": 55,
    "CIRCLE": 21,
    "SOLID": 5,
    "LWPOLYLINE": 103,
    "INSERT": 90,
    "TEXT": 118
  },
  "geometry_checksum": 243588743168.0,
  "bounds": [
    [
      669.72,
      -468.89
    ],
    [
      31152.89,
      24990.74
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
