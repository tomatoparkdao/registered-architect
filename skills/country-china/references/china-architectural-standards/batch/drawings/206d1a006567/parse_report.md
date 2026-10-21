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
    "INSERT": 80,
    "ARC": 53,
    "LINE": 854,
    "SOLID": 44,
    "LWPOLYLINE": 10,
    "CIRCLE": 9,
    "TEXT": 105,
    "MTEXT": 7
  },
  "geometry_checksum": 41815228416.0,
  "bounds": [
    [
      777.92,
      335.69
    ],
    [
      8566.99,
      10597.03
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
