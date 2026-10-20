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
    "LINE": 426,
    "CIRCLE": 2,
    "ARC": 12,
    "LWPOLYLINE": 2,
    "TEXT": 42
  },
  "geometry_checksum": 16506619904.0,
  "bounds": [
    [
      3412.63,
      11862.26
    ],
    [
      8251.66,
      14403.09
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
