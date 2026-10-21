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
    "LINE": 443,
    "INSERT": 30,
    "SOLID": 39,
    "LWPOLYLINE": 30,
    "TEXT": 63,
    "DIMENSION": 48
  },
  "geometry_checksum": 58130579456.0,
  "bounds": [
    [
      -7140.77,
      -101720.58
    ],
    [
      17026.26,
      22581.23
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
