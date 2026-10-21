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
    "LINE": 72,
    "ARC": 3,
    "LWPOLYLINE": 4,
    "HATCH": 5,
    "SPLINE": 1,
    "MTEXT": 8
  },
  "geometry_checksum": 231626368.0,
  "bounds": [
    [
      3136.15,
      -116.52
    ],
    [
      3269.77,
      439.14
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
