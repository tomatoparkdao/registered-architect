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
    "LINE": 506,
    "HATCH": 3,
    "LWPOLYLINE": 55,
    "LEADER": 16,
    "ARC": 9,
    "INSERT": 9,
    "CIRCLE": 12,
    "TEXT": 21,
    "DIMENSION": 14
  },
  "geometry_checksum": 11070236672.0,
  "bounds": [
    [
      235.22,
      1477.92
    ],
    [
      3455.6,
      3125.33
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
