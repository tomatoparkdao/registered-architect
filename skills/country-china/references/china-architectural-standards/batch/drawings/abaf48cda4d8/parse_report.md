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
    "LWPOLYLINE": 20,
    "LINE": 1516,
    "INSERT": 12,
    "ARC": 8,
    "CIRCLE": 4,
    "TEXT": 43,
    "DIMENSION": 28
  },
  "geometry_checksum": 502199713792.0,
  "bounds": [
    [
      18031.61,
      -12161.71
    ],
    [
      47143.28,
      21343.39
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
