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
    "ARC": 151,
    "LINE": 345,
    "SOLID": 82,
    "INSERT": 6,
    "LWPOLYLINE": 7,
    "CIRCLE": 1,
    "TEXT": 78
  },
  "geometry_checksum": 894917440.0,
  "bounds": [
    [
      -351.27,
      -161.57
    ],
    [
      564.5,
      408.48
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
