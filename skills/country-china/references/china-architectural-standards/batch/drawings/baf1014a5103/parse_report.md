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
    "LWPOLYLINE": 155,
    "LINE": 721,
    "CIRCLE": 8,
    "INSERT": 32,
    "HATCH": 3,
    "TEXT": 314,
    "DIMENSION": 197
  },
  "geometry_checksum": 1756087713792.0,
  "bounds": [
    [
      46426.0,
      61608.0
    ],
    [
      128048.9,
      118239.52
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
