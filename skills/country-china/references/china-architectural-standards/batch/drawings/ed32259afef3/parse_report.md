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
    "LINE": 550,
    "HATCH": 14,
    "ARC": 42,
    "LWPOLYLINE": 3,
    "CIRCLE": 6,
    "INSERT": 22,
    "TEXT": 43
  },
  "geometry_checksum": 88724144128.0,
  "bounds": [
    [
      -3063.4,
      -6217.7
    ],
    [
      43313.14,
      59032.2
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
