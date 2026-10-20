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
    "CIRCLE": 8,
    "HATCH": 10,
    "LINE": 656,
    "INSERT": 19,
    "ARC": 33,
    "LWPOLYLINE": 5,
    "TEXT": 161,
    "MTEXT": 10
  },
  "geometry_checksum": 36608565248.0,
  "bounds": [
    [
      1350.73,
      6353.11
    ],
    [
      6946.99,
      10801.66
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
