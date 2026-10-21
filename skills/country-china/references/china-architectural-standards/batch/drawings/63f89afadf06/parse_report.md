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
    "LINE": 186,
    "ARC": 17,
    "LWPOLYLINE": 25,
    "INSERT": 19,
    "CIRCLE": 1,
    "HATCH": 9,
    "MTEXT": 28,
    "TEXT": 2
  },
  "geometry_checksum": 1782195712.0,
  "bounds": [
    [
      2000.07,
      1247.68
    ],
    [
      2464.37,
      2099.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
