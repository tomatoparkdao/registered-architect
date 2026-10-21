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
    "LINE": 364,
    "ARC": 13,
    "HATCH": 3,
    "CIRCLE": 1,
    "LWPOLYLINE": 23,
    "INSERT": 10,
    "TEXT": 111
  },
  "geometry_checksum": 19978512384.0,
  "bounds": [
    [
      983.99,
      671.5
    ],
    [
      28297.16,
      18841.31
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
