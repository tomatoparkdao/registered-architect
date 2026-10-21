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
    "LWPOLYLINE": 620,
    "INSERT": 40,
    "LINE": 254,
    "CIRCLE": 19,
    "SOLID": 8,
    "ARC": 174,
    "TEXT": 124,
    "DIMENSION": 16
  },
  "geometry_checksum": 226441408.0,
  "bounds": [
    [
      -34.41,
      0.36
    ],
    [
      30.82,
      38.94
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
