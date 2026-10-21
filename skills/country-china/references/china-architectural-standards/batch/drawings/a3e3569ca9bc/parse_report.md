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
    "HATCH": 8,
    "LWPOLYLINE": 12,
    "LINE": 196,
    "INSERT": 5,
    "CIRCLE": 7,
    "ARC": 28,
    "TEXT": 46,
    "DIMENSION": 24
  },
  "geometry_checksum": 272892559360.0,
  "bounds": [
    [
      -23561.3,
      431941.72
    ],
    [
      844.26,
      461884.03
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
