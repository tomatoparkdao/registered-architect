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
    "LWPOLYLINE": 16,
    "LINE": 60,
    "INSERT": 3,
    "HATCH": 2,
    "TEXT": 35,
    "DIMENSION": 14
  },
  "geometry_checksum": 241094912.0,
  "bounds": [
    [
      -210.0,
      -24800.0
    ],
    [
      10053.0,
      3010.49
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
