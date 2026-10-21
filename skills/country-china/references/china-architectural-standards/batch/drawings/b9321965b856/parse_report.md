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
    "LINE": 407,
    "HATCH": 1,
    "INSERT": 18,
    "TEXT": 22,
    "DIMENSION": 20
  },
  "geometry_checksum": 63596650496.0,
  "bounds": [
    [
      50963.29,
      16735.85
    ],
    [
      54100.35,
      18832.09
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
