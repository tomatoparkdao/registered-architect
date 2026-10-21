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
    "LINE": 231,
    "LWPOLYLINE": 52,
    "INSERT": 85,
    "HATCH": 1,
    "POLYLINE": 1,
    "CIRCLE": 3,
    "TEXT": 76,
    "MTEXT": 1
  },
  "geometry_checksum": 43903729664.0,
  "bounds": [
    [
      19830.28,
      1185.84
    ],
    [
      37857.43,
      25156.62
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
