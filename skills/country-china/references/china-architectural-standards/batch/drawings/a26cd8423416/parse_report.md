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
    "LINE": 1011,
    "CIRCLE": 17,
    "ARC": 68,
    "INSERT": 35,
    "TEXT": 90,
    "MTEXT": 3
  },
  "geometry_checksum": 61139218432.0,
  "bounds": [
    [
      -28364.95,
      22199.65
    ],
    [
      -8303.33,
      45758.06
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
