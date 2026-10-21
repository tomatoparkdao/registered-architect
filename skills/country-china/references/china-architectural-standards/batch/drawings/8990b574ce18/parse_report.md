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
    "LINE": 192,
    "LWPOLYLINE": 32,
    "HATCH": 5,
    "CIRCLE": 27,
    "INSERT": 40,
    "TEXT": 60
  },
  "geometry_checksum": -24880793600.0,
  "bounds": [
    [
      -40624.09,
      -44064.22
    ],
    [
      -23013.63,
      -34258.44
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
