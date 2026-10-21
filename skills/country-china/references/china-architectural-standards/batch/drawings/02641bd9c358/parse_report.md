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
    "LINE": 73,
    "ARC": 8,
    "INSERT": 28,
    "LWPOLYLINE": 2,
    "HATCH": 1,
    "MTEXT": 14
  },
  "geometry_checksum": 535928.5,
  "bounds": [
    [
      -2.25,
      -3.45
    ],
    [
      21.35,
      9.28
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
