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
    "LWPOLYLINE": 42,
    "INSERT": 9,
    "LINE": 157,
    "TEXT": 35,
    "DIMENSION": 5
  },
  "geometry_checksum": 4821425152.0,
  "bounds": [
    [
      15414.36,
      3566.43
    ],
    [
      18540.28,
      7826.72
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
