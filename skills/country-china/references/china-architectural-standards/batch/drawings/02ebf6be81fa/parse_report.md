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
    "LINE": 1402,
    "LWPOLYLINE": 151,
    "INSERT": 92,
    "ARC": 10,
    "CIRCLE": 4,
    "HATCH": 1,
    "SOLID": 2,
    "TEXT": 133
  },
  "geometry_checksum": 119553974272.0,
  "bounds": [
    [
      -946.24,
      -1785.89
    ],
    [
      5384.77,
      9011.4
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
