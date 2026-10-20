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
    "LINE": 206,
    "SOLID": 49,
    "CIRCLE": 6,
    "ARC": 75,
    "INSERT": 7,
    "LWPOLYLINE": 2,
    "TEXT": 66
  },
  "geometry_checksum": 313528736.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      566.48,
      407.98
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
