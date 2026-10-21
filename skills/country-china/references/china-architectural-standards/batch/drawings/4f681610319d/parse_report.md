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
    "LINE": 469,
    "ARC": 72,
    "LWPOLYLINE": 12,
    "CIRCLE": 6,
    "HATCH": 7,
    "INSERT": 21,
    "TEXT": 29
  },
  "geometry_checksum": 91334606848.0,
  "bounds": [
    [
      18008.83,
      12683.16
    ],
    [
      47361.99,
      57109.74
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
