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
    "LINE": 157,
    "HATCH": 4,
    "LWPOLYLINE": 19,
    "CIRCLE": 1,
    "INSERT": 2,
    "TEXT": 8,
    "DIMENSION": 38
  },
  "geometry_checksum": 1098365184.0,
  "bounds": [
    [
      2111.27,
      -3241.94
    ],
    [
      6674.27,
      1302.3
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
