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
    "LINE": 121,
    "LWPOLYLINE": 34,
    "HATCH": 18,
    "CIRCLE": 1,
    "TEXT": 19,
    "DIMENSION": 38
  },
  "geometry_checksum": 8900726784.0,
  "bounds": [
    [
      -8971.04,
      -8333.99
    ],
    [
      20498.79,
      33340.51
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
