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
    "LINE": 826,
    "INSERT": 85,
    "HATCH": 6,
    "ARC": 18,
    "LWPOLYLINE": 70,
    "CIRCLE": 9,
    "TEXT": 123
  },
  "geometry_checksum": 87443767296.0,
  "bounds": [
    [
      -1759.39,
      -21293.91
    ],
    [
      27069.46,
      19445.88
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
