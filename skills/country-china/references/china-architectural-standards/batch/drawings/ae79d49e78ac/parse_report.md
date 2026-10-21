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
    "LINE": 62,
    "LWPOLYLINE": 5,
    "CIRCLE": 2,
    "HATCH": 1,
    "TEXT": 9,
    "DIMENSION": 16
  },
  "geometry_checksum": 298974016.0,
  "bounds": [
    [
      -4214.5,
      7490.0
    ],
    [
      -1223.93,
      10220.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
