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
    "CIRCLE": 6,
    "ARC": 34,
    "LINE": 1051,
    "HATCH": 12,
    "INSERT": 32,
    "LWPOLYLINE": 2,
    "TEXT": 17,
    "MTEXT": 24
  },
  "geometry_checksum": 4142434615296.0,
  "bounds": [
    [
      96956.3,
      84517.88
    ],
    [
      621141.06,
      380201.72
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
