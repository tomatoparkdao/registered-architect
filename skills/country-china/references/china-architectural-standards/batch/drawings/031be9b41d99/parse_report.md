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
    "LINE": 37,
    "LWPOLYLINE": 14,
    "CIRCLE": 1,
    "INSERT": 1,
    "TEXT": 9,
    "DIMENSION": 9
  },
  "geometry_checksum": 332246464.0,
  "bounds": [
    [
      -93.47,
      3673.84
    ],
    [
      8166.23,
      7314.68
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
