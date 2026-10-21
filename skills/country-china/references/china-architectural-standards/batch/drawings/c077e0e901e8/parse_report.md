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
    "CIRCLE": 9,
    "LINE": 1203,
    "LWPOLYLINE": 144,
    "INSERT": 3,
    "ARC": 78,
    "TEXT": 110,
    "DIMENSION": 39
  },
  "geometry_checksum": -614863470592.0,
  "bounds": [
    [
      -145923.91,
      -3742.64
    ],
    [
      -46603.48,
      64908.77
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
