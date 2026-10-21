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
    "LINE": 397,
    "HATCH": 20,
    "CIRCLE": 4,
    "LWPOLYLINE": 38,
    "ARC": 38,
    "INSERT": 19,
    "TEXT": 18,
    "MTEXT": 11
  },
  "geometry_checksum": 9765745664.0,
  "bounds": [
    [
      2880.28,
      1532.52
    ],
    [
      3717.73,
      2736.56
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
