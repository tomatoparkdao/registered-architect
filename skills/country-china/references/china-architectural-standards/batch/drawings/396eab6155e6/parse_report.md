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
    "LINE": 4151,
    "CIRCLE": 28,
    "ARC": 562,
    "LWPOLYLINE": 31,
    "INSERT": 104,
    "TEXT": 109
  },
  "geometry_checksum": 2886736543744.0,
  "bounds": [
    [
      14969.82,
      15170.54
    ],
    [
      17594.84,
      18665.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
