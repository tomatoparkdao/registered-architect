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
    "LINE": 136,
    "HATCH": 7,
    "INSERT": 7,
    "ARC": 15,
    "CIRCLE": 6,
    "TEXT": 16,
    "DIMENSION": 11
  },
  "geometry_checksum": -55119151104.0,
  "bounds": [
    [
      -153805.66,
      -158074.7
    ],
    [
      153096.42,
      -156853.77
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
