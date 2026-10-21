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
    "LWPOLYLINE": 93,
    "LINE": 1845,
    "LEADER": 40,
    "INSERT": 123,
    "CIRCLE": 16,
    "HATCH": 17,
    "ARC": 84,
    "TEXT": 96
  },
  "geometry_checksum": 224953073664.0,
  "bounds": [
    [
      1019.51,
      956.25
    ],
    [
      10144.41,
      12503.77
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
