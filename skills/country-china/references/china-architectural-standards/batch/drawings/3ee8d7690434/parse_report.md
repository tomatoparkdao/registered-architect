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
    "LINE": 397,
    "LWPOLYLINE": 30,
    "INSERT": 45,
    "HATCH": 1,
    "ARC": 7,
    "CIRCLE": 4,
    "TEXT": 51
  },
  "geometry_checksum": 8202795008.0,
  "bounds": [
    [
      -38820.78,
      -126010.05
    ],
    [
      8580.88,
      7961.69
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
