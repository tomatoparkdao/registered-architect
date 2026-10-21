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
    "LINE": 920,
    "CIRCLE": 6,
    "ARC": 85,
    "LWPOLYLINE": 1,
    "HATCH": 12,
    "INSERT": 67,
    "TEXT": 84
  },
  "geometry_checksum": 101810192384.0,
  "bounds": [
    [
      8963.22,
      -9738.71
    ],
    [
      36501.66,
      11751.96
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
