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
    "LINE": 300,
    "ARC": 8,
    "LWPOLYLINE": 16,
    "CIRCLE": 4,
    "TEXT": 1,
    "DIMENSION": 10
  },
  "geometry_checksum": 20815476736.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      15578.01,
      27311.86
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
