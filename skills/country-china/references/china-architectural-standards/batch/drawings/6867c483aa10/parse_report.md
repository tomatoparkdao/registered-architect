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
    "LINE": 62,
    "INSERT": 4,
    "HATCH": 7,
    "LWPOLYLINE": 9,
    "TEXT": 11,
    "DIMENSION": 5
  },
  "geometry_checksum": 1276492160.0,
  "bounds": [
    [
      -7140.77,
      15029.91
    ],
    [
      8322.65,
      18915.52
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
