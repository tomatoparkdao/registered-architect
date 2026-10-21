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
    "INSERT": 9,
    "LINE": 457,
    "LWPOLYLINE": 33,
    "CIRCLE": 4,
    "SOLID": 3,
    "TEXT": 79,
    "DIMENSION": 29
  },
  "geometry_checksum": 1347485696000.0,
  "bounds": [
    [
      515463.81,
      38775.36
    ],
    [
      545163.81,
      80825.36
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
