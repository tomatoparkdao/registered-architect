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
    "INSERT": 61,
    "LINE": 493,
    "CIRCLE": 13,
    "LWPOLYLINE": 10,
    "HATCH": 16,
    "ARC": 4,
    "TEXT": 65,
    "MTEXT": 1
  },
  "geometry_checksum": 12676826112.0,
  "bounds": [
    [
      920.56,
      335.7
    ],
    [
      8311.68,
      6960.73
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
