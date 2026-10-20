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
    "LINE": 353,
    "LWPOLYLINE": 93,
    "CIRCLE": 23,
    "HATCH": 19,
    "LEADER": 39,
    "ARC": 43,
    "TEXT": 56,
    "DIMENSION": 32
  },
  "geometry_checksum": 80528736256.0,
  "bounds": [
    [
      1357.53,
      2071.23
    ],
    [
      14331.3,
      20019.66
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
