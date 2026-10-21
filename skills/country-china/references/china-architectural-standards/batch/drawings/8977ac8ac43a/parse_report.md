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
    "LINE": 1029,
    "CIRCLE": 4,
    "ARC": 3,
    "HATCH": 1,
    "INSERT": 4,
    "TEXT": 36
  },
  "geometry_checksum": 49478381568.0,
  "bounds": [
    [
      -17517.63,
      -12910.56
    ],
    [
      14752.42,
      14664.59
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
