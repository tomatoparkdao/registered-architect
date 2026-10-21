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
    "LINE": 552,
    "INSERT": 86,
    "LWPOLYLINE": 12,
    "HATCH": 13,
    "ARC": 61,
    "CIRCLE": 30,
    "TEXT": 81
  },
  "geometry_checksum": 422862356480.0,
  "bounds": [
    [
      59857.74,
      28284.55
    ],
    [
      129326.79,
      129941.07
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
