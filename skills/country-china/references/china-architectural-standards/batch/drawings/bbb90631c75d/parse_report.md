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
    "LINE": 1783,
    "LWPOLYLINE": 27,
    "INSERT": 4,
    "CIRCLE": 1,
    "TEXT": 23,
    "DIMENSION": 7
  },
  "geometry_checksum": 23923101696.0,
  "bounds": [
    [
      -1667.87,
      -24239.57
    ],
    [
      8366.42,
      2510.74
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
