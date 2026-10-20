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
    "INSERT": 264,
    "LINE": 7053,
    "LWPOLYLINE": 203,
    "ARC": 89,
    "CIRCLE": 178,
    "HATCH": 159,
    "TEXT": 278,
    "MTEXT": 402,
    "DIMENSION": 407
  },
  "geometry_checksum": 73112532025344.0,
  "bounds": [
    [
      -37564.94,
      -2059335.5
    ],
    [
      1133840.38,
      144857.95
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
