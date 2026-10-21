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
    "CIRCLE": 10,
    "LINE": 816,
    "ARC": 5,
    "SPLINE": 8,
    "INSERT": 48,
    "LWPOLYLINE": 2,
    "TEXT": 42
  },
  "geometry_checksum": 16769761280.0,
  "bounds": [
    [
      3205.06,
      -2378.63
    ],
    [
      7036.9,
      3092.75
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
