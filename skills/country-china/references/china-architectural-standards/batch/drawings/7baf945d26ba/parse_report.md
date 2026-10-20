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
    "LEADER": 32,
    "LINE": 370,
    "LWPOLYLINE": 18,
    "INSERT": 22,
    "HATCH": 19,
    "ARC": 352,
    "CIRCLE": 4,
    "TEXT": 47,
    "DIMENSION": 65
  },
  "geometry_checksum": 22110814208.0,
  "bounds": [
    [
      118.61,
      365.09
    ],
    [
      4989.09,
      7003.51
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
