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
    "LINE": 138,
    "CIRCLE": 3,
    "HATCH": 5,
    "LWPOLYLINE": 5,
    "SOLID": 34,
    "INSERT": 1,
    "TEXT": 40,
    "DIMENSION": 3
  },
  "geometry_checksum": 4184484608.0,
  "bounds": [
    [
      6369.5,
      8883.64
    ],
    [
      9806.79,
      11781.17
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
