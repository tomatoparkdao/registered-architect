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
    "LEADER": 26,
    "LWPOLYLINE": 32,
    "ARC": 32,
    "HATCH": 10,
    "LINE": 137,
    "CIRCLE": 4,
    "INSERT": 41,
    "TEXT": 40,
    "DIMENSION": 35
  },
  "geometry_checksum": 2705480192.0,
  "bounds": [
    [
      77.59,
      245.88
    ],
    [
      3341.03,
      4703.65
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
