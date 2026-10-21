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
    "LINE": 6810,
    "CIRCLE": 118,
    "ARC": 260,
    "LWPOLYLINE": 1,
    "TEXT": 15
  },
  "geometry_checksum": 28764751872.0,
  "bounds": [
    [
      -22.3,
      -421.6
    ],
    [
      193.05,
      483.87
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
