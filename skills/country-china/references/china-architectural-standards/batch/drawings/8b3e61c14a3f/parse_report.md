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
    "LWPOLYLINE": 78,
    "CIRCLE": 2,
    "LINE": 98,
    "ARC": 6,
    "INSERT": 8,
    "TEXT": 955
  },
  "geometry_checksum": 4611220480.0,
  "bounds": [
    [
      -205.58,
      16.46
    ],
    [
      3081.63,
      2842.27
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
