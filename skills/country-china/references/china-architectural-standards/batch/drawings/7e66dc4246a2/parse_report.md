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
    "LINE": 905,
    "CIRCLE": 24,
    "ARC": 18,
    "HATCH": 13,
    "LWPOLYLINE": 24,
    "INSERT": 4,
    "TEXT": 66
  },
  "geometry_checksum": 47583092736.0,
  "bounds": [
    [
      1779.9,
      4625.85
    ],
    [
      7997.48,
      9165.49
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
