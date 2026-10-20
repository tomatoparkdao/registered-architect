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
    "CIRCLE": 9,
    "ARC": 8,
    "LINE": 81,
    "LWPOLYLINE": 353,
    "HATCH": 37
  },
  "geometry_checksum": 3007801600.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      1200.0,
      2000.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
