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
    "LINE": 343,
    "LWPOLYLINE": 45,
    "CIRCLE": 1,
    "TEXT": 9,
    "DIMENSION": 8
  },
  "geometry_checksum": 34712043520.0,
  "bounds": [
    [
      18363.65,
      26321.63
    ],
    [
      19889.85,
      28771.91
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
