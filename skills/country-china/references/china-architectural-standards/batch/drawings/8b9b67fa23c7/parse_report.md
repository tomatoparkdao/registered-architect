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
    "LINE": 1459,
    "ARC": 319,
    "CIRCLE": 28,
    "HATCH": 6,
    "LWPOLYLINE": 14,
    "TEXT": 50,
    "MTEXT": 8
  },
  "geometry_checksum": 1732501438464.0,
  "bounds": [
    [
      113410.28,
      39619.42
    ],
    [
      113998.79,
      40407.85
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
