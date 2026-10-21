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
    "LWPOLYLINE": 167,
    "LINE": 2234,
    "HATCH": 43,
    "CIRCLE": 14,
    "INSERT": 200,
    "ARC": 14,
    "TEXT": 194
  },
  "geometry_checksum": 799088443392.0,
  "bounds": [
    [
      934.39,
      -3695.67
    ],
    [
      26416.77,
      9251.28
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
