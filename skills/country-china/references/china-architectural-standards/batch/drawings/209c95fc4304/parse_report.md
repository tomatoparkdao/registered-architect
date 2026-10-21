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
    "LINE": 56,
    "LWPOLYLINE": 9,
    "INSERT": 2,
    "HATCH": 2,
    "TEXT": 7,
    "DIMENSION": 9
  },
  "geometry_checksum": 40596128.0,
  "bounds": [
    [
      -1988.76,
      1294.11
    ],
    [
      613.63,
      2452.15
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
