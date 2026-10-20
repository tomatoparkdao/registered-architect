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
    "LINE": 1139,
    "CIRCLE": 13,
    "ARC": 34,
    "LWPOLYLINE": 15,
    "INSERT": 43,
    "HATCH": 14,
    "TEXT": 158,
    "MTEXT": 17,
    "DIMENSION": 7
  },
  "geometry_checksum": 128414679040.0,
  "bounds": [
    [
      3072.42,
      4503.86
    ],
    [
      13568.9,
      11816.88
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
