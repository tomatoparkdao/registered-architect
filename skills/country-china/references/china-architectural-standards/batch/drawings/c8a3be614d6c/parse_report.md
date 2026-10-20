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
    "LWPOLYLINE": 145,
    "LINE": 24,
    "ARC": 258,
    "CIRCLE": 4,
    "HATCH": 2,
    "INSERT": 1
  },
  "geometry_checksum": 89230876672.0,
  "bounds": [
    [
      877.67,
      745.74
    ],
    [
      1937.67,
      2925.74
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
