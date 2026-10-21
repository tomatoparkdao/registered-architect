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
    "LINE": 257,
    "LWPOLYLINE": 12,
    "ARC": 208,
    "HATCH": 4,
    "CIRCLE": 8,
    "INSERT": 4,
    "TEXT": 40,
    "MTEXT": 2
  },
  "geometry_checksum": 117382332416.0,
  "bounds": [
    [
      111966.9,
      38886.3
    ],
    [
      112561.14,
      39822.9
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
