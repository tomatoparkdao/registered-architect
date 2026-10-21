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
    "LINE": 202,
    "INSERT": 14,
    "HATCH": 12,
    "CIRCLE": 4,
    "ARC": 30,
    "ELLIPSE": 2,
    "LWPOLYLINE": 6,
    "TEXT": 1,
    "MTEXT": 11
  },
  "geometry_checksum": 1018668160.0,
  "bounds": [
    [
      2474.84,
      815.51
    ],
    [
      2681.77,
      1113.31
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
