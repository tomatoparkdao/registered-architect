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
    "LWPOLYLINE": 6,
    "LINE": 74,
    "CIRCLE": 4,
    "INSERT": 19,
    "TEXT": 3,
    "MTEXT": 10,
    "DIMENSION": 2
  },
  "geometry_checksum": 101022912.0,
  "bounds": [
    [
      -4292.16,
      -5825.9
    ],
    [
      3274.29,
      6828.21
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
