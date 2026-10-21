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
    "LINE": 337,
    "INSERT": 38,
    "CIRCLE": 12,
    "ARC": 19,
    "TEXT": 66
  },
  "geometry_checksum": 6800829952.0,
  "bounds": [
    [
      87.41,
      1166.36
    ],
    [
      7002.49,
      11498.81
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
