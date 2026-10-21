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
    "LINE": 55,
    "LWPOLYLINE": 9,
    "INSERT": 1,
    "HATCH": 2,
    "TEXT": 6,
    "DIMENSION": 7
  },
  "geometry_checksum": 892886528.0,
  "bounds": [
    [
      10700.0,
      2692.68
    ],
    [
      22145.24,
      9700.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
