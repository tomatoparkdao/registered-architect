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
    "LINE": 857,
    "CIRCLE": 43,
    "ARC": 41,
    "INSERT": 6,
    "LWPOLYLINE": 3,
    "HATCH": 4,
    "TEXT": 79
  },
  "geometry_checksum": 42456702976.0,
  "bounds": [
    [
      2599.74,
      1230.86
    ],
    [
      13196.69,
      6066.38
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
