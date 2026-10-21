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
    "LINE": 380,
    "LWPOLYLINE": 52,
    "CIRCLE": 5,
    "ARC": 124,
    "HATCH": 1,
    "TEXT": 38
  },
  "geometry_checksum": 872165120.0,
  "bounds": [
    [
      484.27,
      153.17
    ],
    [
      571.55,
      221.51
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
