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
    "LINE": 984,
    "INSERT": 279,
    "LWPOLYLINE": 30,
    "HATCH": 20,
    "CIRCLE": 17,
    "ARC": 1,
    "MTEXT": 123,
    "TEXT": 5,
    "DIMENSION": 31
  },
  "geometry_checksum": 99713286144.0,
  "bounds": [
    [
      2913.06,
      -4050.62
    ],
    [
      15513.06,
      14060.94
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
