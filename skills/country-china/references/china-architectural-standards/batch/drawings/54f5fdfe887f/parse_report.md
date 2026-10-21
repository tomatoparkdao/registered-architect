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
    "LINE": 151,
    "LWPOLYLINE": 87,
    "CIRCLE": 8,
    "INSERT": 7,
    "HATCH": 14,
    "MTEXT": 12,
    "TEXT": 3
  },
  "geometry_checksum": 5545235456.0,
  "bounds": [
    [
      1609.82,
      -25234.47
    ],
    [
      7878.31,
      3596.18
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
