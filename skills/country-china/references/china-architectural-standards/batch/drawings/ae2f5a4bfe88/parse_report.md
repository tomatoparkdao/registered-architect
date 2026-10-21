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
    "LWPOLYLINE": 77,
    "CIRCLE": 11,
    "INSERT": 1,
    "TEXT": 33,
    "DIMENSION": 3
  },
  "geometry_checksum": 34583855104.0,
  "bounds": [
    [
      287818.31,
      67136.1
    ],
    [
      305679.12,
      77425.48
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
