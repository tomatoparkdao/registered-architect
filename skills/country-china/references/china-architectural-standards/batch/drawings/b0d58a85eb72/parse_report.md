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
    "LWPOLYLINE": 60,
    "LINE": 219,
    "ARC": 9,
    "CIRCLE": 13,
    "TEXT": 3185
  },
  "geometry_checksum": 50667544576.0,
  "bounds": [
    [
      -355.19,
      -245.81
    ],
    [
      4316.76,
      3007.21
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
