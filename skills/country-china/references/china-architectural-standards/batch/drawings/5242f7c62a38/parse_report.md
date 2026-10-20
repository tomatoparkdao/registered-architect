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
    "LINE": 452,
    "LWPOLYLINE": 44,
    "INSERT": 22,
    "TEXT": 69,
    "DIMENSION": 68
  },
  "geometry_checksum": 105343664128.0,
  "bounds": [
    [
      -9956.49,
      -8462.04
    ],
    [
      59881.97,
      35528.79
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
