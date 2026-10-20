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
    "LINE": 206,
    "ARC": 51,
    "SOLID": 52,
    "CIRCLE": 3,
    "INSERT": 6,
    "LWPOLYLINE": 2,
    "TEXT": 61
  },
  "geometry_checksum": 196814672.0,
  "bounds": [
    [
      -8.37,
      -12.46
    ],
    [
      397.88,
      289.49
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
