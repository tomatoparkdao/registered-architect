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
    "LWPOLYLINE": 52,
    "LINE": 196,
    "CIRCLE": 13,
    "ARC": 2,
    "SOLID": 2,
    "TEXT": 2950
  },
  "geometry_checksum": 38605103104.0,
  "bounds": [
    [
      -355.19,
      -334.2
    ],
    [
      3883.79,
      2821.07
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
