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
    "INSERT": 7,
    "LINE": 137,
    "ARC": 37,
    "HATCH": 13,
    "LWPOLYLINE": 26,
    "CIRCLE": 11,
    "TEXT": 26
  },
  "geometry_checksum": 669611196416.0,
  "bounds": [
    [
      127626.43,
      94547.26
    ],
    [
      170828.81,
      154002.03
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
