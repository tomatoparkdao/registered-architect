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
    "LINE": 448,
    "LWPOLYLINE": 10,
    "HATCH": 10,
    "SOLID": 1,
    "CIRCLE": 4,
    "INSERT": 50,
    "TEXT": 60
  },
  "geometry_checksum": 31311880192.0,
  "bounds": [
    [
      -3992.75,
      -6679.42
    ],
    [
      21201.84,
      24171.85
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
