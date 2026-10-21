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
    "LINE": 40,
    "LWPOLYLINE": 14,
    "ARC": 2,
    "HATCH": 3,
    "TEXT": 16,
    "DIMENSION": 7
  },
  "geometry_checksum": 18714848.0,
  "bounds": [
    [
      -1378.89,
      366.38
    ],
    [
      -177.84,
      1503.08
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
