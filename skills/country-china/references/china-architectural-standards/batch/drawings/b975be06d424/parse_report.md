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
    "LEADER": 30,
    "HATCH": 17,
    "LINE": 319,
    "ARC": 173,
    "LWPOLYLINE": 39,
    "CIRCLE": 4,
    "INSERT": 37,
    "TEXT": 44,
    "DIMENSION": 28
  },
  "geometry_checksum": 7554897920.0,
  "bounds": [
    [
      -1891.0,
      73.12
    ],
    [
      4713.28,
      4265.41
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
