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
    "LINE": 59,
    "LWPOLYLINE": 3,
    "INSERT": 6,
    "SOLID": 7,
    "TEXT": 15,
    "DIMENSION": 6
  },
  "geometry_checksum": 337589888.0,
  "bounds": [
    [
      0.0,
      -2504.39
    ],
    [
      5626.77,
      5441.77
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
