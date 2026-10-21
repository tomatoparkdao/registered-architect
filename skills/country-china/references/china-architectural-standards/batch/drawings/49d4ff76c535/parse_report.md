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
    "LINE": 36,
    "POLYLINE": 75,
    "CIRCLE": 11,
    "LWPOLYLINE": 1,
    "TEXT": 30
  },
  "geometry_checksum": 33451728896.0,
  "bounds": [
    [
      247223.0,
      77608.1
    ],
    [
      261523.0,
      87381.18
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
