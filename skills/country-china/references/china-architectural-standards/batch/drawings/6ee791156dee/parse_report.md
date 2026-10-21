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
    "LINE": 386,
    "CIRCLE": 33,
    "ARC": 31,
    "INSERT": 15,
    "TEXT": 63,
    "MTEXT": 2
  },
  "geometry_checksum": 1581022848.0,
  "bounds": [
    [
      343.29,
      -1538.96
    ],
    [
      2530.21,
      2135.68
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
