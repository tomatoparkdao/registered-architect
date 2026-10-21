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
    "LINE": 421,
    "LWPOLYLINE": 136,
    "HATCH": 19,
    "INSERT": 12,
    "TEXT": 26,
    "DIMENSION": 30
  },
  "geometry_checksum": 53033652224.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      13235.53,
      18751.79
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
