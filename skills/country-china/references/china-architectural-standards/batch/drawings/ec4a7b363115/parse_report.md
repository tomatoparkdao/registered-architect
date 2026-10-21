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
    "LWPOLYLINE": 148,
    "LINE": 706,
    "INSERT": 39,
    "ARC": 32,
    "HATCH": 56,
    "CIRCLE": 24,
    "TEXT": 123,
    "DIMENSION": 135
  },
  "geometry_checksum": 2543186345984.0,
  "bounds": [
    [
      0.0,
      -18440.94
    ],
    [
      228466.33,
      21345.11
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
