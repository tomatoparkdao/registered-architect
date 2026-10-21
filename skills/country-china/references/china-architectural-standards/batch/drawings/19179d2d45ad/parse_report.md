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
    "CIRCLE": 4,
    "LINE": 204,
    "LWPOLYLINE": 16,
    "ARC": 4,
    "HATCH": 9,
    "INSERT": 40,
    "TEXT": 28
  },
  "geometry_checksum": 2027833600.0,
  "bounds": [
    [
      721.33,
      272.04
    ],
    [
      3168.18,
      3277.02
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
