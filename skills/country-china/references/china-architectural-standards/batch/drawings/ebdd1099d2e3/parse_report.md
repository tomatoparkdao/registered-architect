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
    "INSERT": 29,
    "LINE": 233,
    "CIRCLE": 6,
    "HATCH": 3,
    "LWPOLYLINE": 8,
    "ARC": 4,
    "TEXT": 28
  },
  "geometry_checksum": -8561713664.0,
  "bounds": [
    [
      0.0,
      -24480.97
    ],
    [
      11106.23,
      0.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
