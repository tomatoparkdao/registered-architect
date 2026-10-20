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
    "LINE": 128,
    "CIRCLE": 2,
    "LWPOLYLINE": 29,
    "TEXT": 835,
    "MTEXT": 12
  },
  "geometry_checksum": 279266033664.0,
  "bounds": [
    [
      -59169.37,
      -74537.83
    ],
    [
      287162.47,
      -890.01
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
