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
    "INSERT": 16,
    "LINE": 599,
    "ARC": 82,
    "CIRCLE": 18,
    "HATCH": 11,
    "LWPOLYLINE": 10,
    "SPLINE": 2,
    "TEXT": 51
  },
  "geometry_checksum": 31886123008.0,
  "bounds": [
    [
      -720.61,
      6841.98
    ],
    [
      9033.29,
      11264.08
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
