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
    "LINE": 3407,
    "INSERT": 35,
    "LWPOLYLINE": 74,
    "CIRCLE": 77,
    "HATCH": 2,
    "TEXT": 30,
    "DIMENSION": 2
  },
  "geometry_checksum": 309802299293696.0,
  "bounds": [
    [
      3325320.75,
      2274627.75
    ],
    [
      3387714.25,
      2303779.5
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
