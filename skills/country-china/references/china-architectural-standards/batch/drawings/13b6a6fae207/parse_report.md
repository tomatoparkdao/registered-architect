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
    "POLYLINE": 88,
    "LINE": 41,
    "CIRCLE": 15,
    "LWPOLYLINE": 1,
    "TEXT": 37
  },
  "geometry_checksum": 46479835136.0,
  "bounds": [
    [
      265375.59,
      76811.29
    ],
    [
      279899.31,
      86607.55
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
