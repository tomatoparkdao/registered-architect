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
    "LWPOLYLINE": 62,
    "LINE": 585,
    "CIRCLE": 56,
    "ARC": 24,
    "HATCH": 6,
    "INSERT": 18,
    "MTEXT": 21,
    "TEXT": 14
  },
  "geometry_checksum": 22107463680.0,
  "bounds": [
    [
      3234.11,
      3083.51
    ],
    [
      4407.72,
      4605.88
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
