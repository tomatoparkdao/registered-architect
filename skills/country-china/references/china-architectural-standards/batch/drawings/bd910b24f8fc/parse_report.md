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
    "LWPOLYLINE": 43,
    "LINE": 251,
    "INSERT": 18,
    "TEXT": 46,
    "DIMENSION": 10
  },
  "geometry_checksum": 9287481344.0,
  "bounds": [
    [
      10698.39,
      -235.29
    ],
    [
      15222.51,
      8986.52
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
