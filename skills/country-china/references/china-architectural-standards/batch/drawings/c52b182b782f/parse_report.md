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
    "INSERT": 114,
    "LINE": 869,
    "POLYLINE": 43,
    "SOLID": 10,
    "ARC": 7,
    "HATCH": 2,
    "LWPOLYLINE": 1,
    "CIRCLE": 1,
    "TEXT": 170
  },
  "geometry_checksum": -922341933056.0,
  "bounds": [
    [
      -48934.46,
      -272008.59
    ],
    [
      65033.69,
      0.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
