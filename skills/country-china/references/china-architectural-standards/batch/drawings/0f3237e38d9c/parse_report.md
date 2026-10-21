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
    "INSERT": 38,
    "LWPOLYLINE": 703,
    "LINE": 758,
    "SOLID": 49,
    "POLYLINE": 12,
    "ARC": 27,
    "TEXT": 106,
    "DIMENSION": 22
  },
  "geometry_checksum": -143530336.0,
  "bounds": [
    [
      -20.66,
      -21.91
    ],
    [
      23.72,
      15.57
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
