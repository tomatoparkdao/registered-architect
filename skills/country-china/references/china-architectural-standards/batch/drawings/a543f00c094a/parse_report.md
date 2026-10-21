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
    "CIRCLE": 4,
    "LWPOLYLINE": 15,
    "LINE": 90,
    "INSERT": 24,
    "MTEXT": 13,
    "TEXT": 4,
    "DIMENSION": 3
  },
  "geometry_checksum": 17034204.0,
  "bounds": [
    [
      -4238.15,
      -5971.92
    ],
    [
      3481.6,
      5690.49
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
