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
    "LINE": 157,
    "ARC": 6,
    "CIRCLE": 3,
    "HATCH": 21,
    "INSERT": 28,
    "LWPOLYLINE": 2,
    "TEXT": 24
  },
  "geometry_checksum": 27508793344.0,
  "bounds": [
    [
      14260.61,
      8857.02
    ],
    [
      64827.02,
      89052.79
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
