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
    "LWPOLYLINE": 11,
    "LINE": 478,
    "CIRCLE": 13,
    "ARC": 74,
    "HATCH": 4,
    "INSERT": 8,
    "TEXT": 73
  },
  "geometry_checksum": 139813421056.0,
  "bounds": [
    [
      61278.25,
      26775.45
    ],
    [
      63826.22,
      30264.85
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
