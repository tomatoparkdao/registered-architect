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
    "INSERT": 165,
    "LINE": 961,
    "LWPOLYLINE": 18,
    "CIRCLE": 4,
    "ARC": 15,
    "SOLID": 7,
    "TEXT": 135
  },
  "geometry_checksum": 197658787840.0,
  "bounds": [
    [
      -394001.12,
      -249133.91
    ],
    [
      31413.43,
      34610.47
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
