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
    "LINE": 51,
    "HATCH": 8,
    "CIRCLE": 8,
    "LWPOLYLINE": 4,
    "INSERT": 2,
    "TEXT": 12,
    "DIMENSION": 11
  },
  "geometry_checksum": 1451095040.0,
  "bounds": [
    [
      13044.66,
      19255.51
    ],
    [
      14861.97,
      22185.35
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
