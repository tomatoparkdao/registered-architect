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
    "LINE": 556,
    "LWPOLYLINE": 12,
    "HATCH": 29,
    "ARC": 140,
    "CIRCLE": 6,
    "INSERT": 10,
    "TEXT": 45
  },
  "geometry_checksum": 72787771392.0,
  "bounds": [
    [
      493.57,
      6547.34
    ],
    [
      29043.31,
      35680.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
