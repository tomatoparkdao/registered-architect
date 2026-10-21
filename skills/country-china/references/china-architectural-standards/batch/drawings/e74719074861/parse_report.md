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
    "LINE": 367,
    "LWPOLYLINE": 2,
    "ARC": 15,
    "CIRCLE": 6,
    "HATCH": 3,
    "LEADER": 6,
    "INSERT": 2,
    "TEXT": 4,
    "MTEXT": 6,
    "DIMENSION": 13
  },
  "geometry_checksum": 208639295488.0,
  "bounds": [
    [
      274616.5,
      -2098.37
    ],
    [
      280889.09,
      -699.01
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
