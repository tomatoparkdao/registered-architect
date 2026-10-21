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
    "LINE": 61,
    "CIRCLE": 2,
    "LWPOLYLINE": 6,
    "INSERT": 4,
    "ARC": 1,
    "TEXT": 1,
    "MTEXT": 5,
    "DIMENSION": 6
  },
  "geometry_checksum": 63410440.0,
  "bounds": [
    [
      -4282.67,
      -4603.07
    ],
    [
      6117.45,
      4997.85
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
