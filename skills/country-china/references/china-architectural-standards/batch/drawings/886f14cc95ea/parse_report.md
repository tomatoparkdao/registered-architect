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
    "LINE": 185,
    "CIRCLE": 3,
    "ARC": 12,
    "LWPOLYLINE": 9,
    "INSERT": 5,
    "TEXT": 56,
    "MTEXT": 1
  },
  "geometry_checksum": 4355277824.0,
  "bounds": [
    [
      2727.34,
      9470.01
    ],
    [
      11227.0,
      13093.17
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
