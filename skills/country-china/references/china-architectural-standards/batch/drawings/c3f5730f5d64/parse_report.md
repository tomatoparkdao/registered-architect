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
    "LWPOLYLINE": 169,
    "CIRCLE": 2,
    "LINE": 117,
    "ARC": 18,
    "TEXT": 4023
  },
  "geometry_checksum": 61353172992.0,
  "bounds": [
    [
      -234.38,
      -18.99
    ],
    [
      3274.02,
      3258.75
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
