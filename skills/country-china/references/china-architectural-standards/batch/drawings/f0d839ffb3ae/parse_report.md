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
    "LINE": 160,
    "HATCH": 19,
    "CIRCLE": 11,
    "LWPOLYLINE": 35,
    "INSERT": 1,
    "TEXT": 18,
    "DIMENSION": 22
  },
  "geometry_checksum": 895884672.0,
  "bounds": [
    [
      11.57,
      -1446.98
    ],
    [
      4324.64,
      2914.38
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
