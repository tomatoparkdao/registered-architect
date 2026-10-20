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
    "LINE": 129,
    "LWPOLYLINE": 56,
    "CIRCLE": 1,
    "ARC": 9,
    "INSERT": 15,
    "TEXT": 216
  },
  "geometry_checksum": 421083840.0,
  "bounds": [
    [
      262.77,
      -327.71
    ],
    [
      1560.99,
      1320.98
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
