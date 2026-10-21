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
    "LWPOLYLINE": 219,
    "INSERT": 28,
    "CIRCLE": 7,
    "LINE": 678,
    "HATCH": 56,
    "LEADER": 51,
    "ARC": 198,
    "MTEXT": 52,
    "TEXT": 65,
    "DIMENSION": 121
  },
  "geometry_checksum": 15122340773888.0,
  "bounds": [
    [
      -1248371.75,
      -6529409.0
    ],
    [
      7795258.0,
      983613.19
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
