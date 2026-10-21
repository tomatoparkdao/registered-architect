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
    "INSERT": 2,
    "ARC": 19,
    "LWPOLYLINE": 47,
    "LINE": 118,
    "CIRCLE": 7,
    "HATCH": 1,
    "TEXT": 24
  },
  "geometry_checksum": 65936580.0,
  "bounds": [
    [
      -4.6,
      -118.9
    ],
    [
      102.23,
      83.55
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
