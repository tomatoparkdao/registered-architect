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
    "ARC": 9,
    "LWPOLYLINE": 228,
    "LINE": 674,
    "CIRCLE": 6,
    "INSERT": 121,
    "HATCH": 6,
    "TEXT": 113
  },
  "geometry_checksum": -985720029184.0,
  "bounds": [
    [
      -221537.94,
      -78856.17
    ],
    [
      -21341.7,
      -4543.7
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
