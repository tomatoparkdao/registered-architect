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
    "CIRCLE": 1,
    "LINE": 42,
    "HATCH": 5,
    "LWPOLYLINE": 11,
    "TEXT": 14
  },
  "geometry_checksum": 349041536.0,
  "bounds": [
    [
      7761.32,
      10353.96
    ],
    [
      9832.4,
      11482.54
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
