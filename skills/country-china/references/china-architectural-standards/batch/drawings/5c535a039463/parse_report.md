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
    "LINE": 46,
    "LWPOLYLINE": 7,
    "INSERT": 2,
    "HATCH": 8,
    "CIRCLE": 7,
    "TEXT": 8,
    "DIMENSION": 3
  },
  "geometry_checksum": 544847360.0,
  "bounds": [
    [
      16083.74,
      4696.89
    ],
    [
      18186.17,
      6138.79
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
