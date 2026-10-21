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
    "LINE": 159,
    "LWPOLYLINE": 99,
    "INSERT": 3,
    "CIRCLE": 9,
    "TEXT": 59,
    "DIMENSION": 29
  },
  "geometry_checksum": 61114023936.0,
  "bounds": [
    [
      128024.12,
      -47987.31
    ],
    [
      165667.64,
      -33916.52
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
