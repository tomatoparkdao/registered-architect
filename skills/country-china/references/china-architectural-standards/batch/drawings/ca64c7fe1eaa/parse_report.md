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
    "LINE": 208,
    "INSERT": 9,
    "LWPOLYLINE": 2,
    "CIRCLE": 1,
    "HATCH": 1,
    "TEXT": 13,
    "DIMENSION": 5
  },
  "geometry_checksum": 15653797888.0,
  "bounds": [
    [
      54908.96,
      14550.04
    ],
    [
      56352.76,
      15605.67
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
