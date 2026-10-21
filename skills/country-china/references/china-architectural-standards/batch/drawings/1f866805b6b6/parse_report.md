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
    "LINE": 250,
    "LWPOLYLINE": 66,
    "CIRCLE": 6,
    "INSERT": 20,
    "HATCH": 10,
    "ARC": 18,
    "MTEXT": 24,
    "TEXT": 8
  },
  "geometry_checksum": 18759108608.0,
  "bounds": [
    [
      8227.88,
      -23495.75
    ],
    [
      12745.25,
      33816.86
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
