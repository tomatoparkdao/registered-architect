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
    "LINE": 1068,
    "LWPOLYLINE": 132,
    "ARC": 15,
    "CIRCLE": 30,
    "TEXT": 141,
    "DIMENSION": 63
  },
  "geometry_checksum": -18446252032.0,
  "bounds": [
    [
      -11437.0,
      -3641.0
    ],
    [
      5114.75,
      2048.67
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
