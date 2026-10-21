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
    "LWPOLYLINE": 45,
    "LINE": 496,
    "CIRCLE": 14,
    "HATCH": 71,
    "ARC": 54,
    "INSERT": 3,
    "TEXT": 74,
    "MTEXT": 65
  },
  "geometry_checksum": 1853028040704.0,
  "bounds": [
    [
      -42187.98,
      -90321.98
    ],
    [
      863639.5,
      154341.72
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
