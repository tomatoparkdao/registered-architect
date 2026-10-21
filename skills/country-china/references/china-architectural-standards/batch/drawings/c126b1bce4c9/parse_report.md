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
    "CIRCLE": 16,
    "LINE": 1051,
    "ARC": 32,
    "LWPOLYLINE": 20,
    "INSERT": 22,
    "SPLINE": 2,
    "TEXT": 105,
    "MTEXT": 5
  },
  "geometry_checksum": 91752906752.0,
  "bounds": [
    [
      819.36,
      5902.22
    ],
    [
      9531.71,
      12607.32
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
