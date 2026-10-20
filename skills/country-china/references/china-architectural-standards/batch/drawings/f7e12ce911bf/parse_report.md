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
    "LINE": 631,
    "CIRCLE": 13,
    "SOLID": 103,
    "ARC": 90,
    "INSERT": 13,
    "LWPOLYLINE": 4,
    "TEXT": 128
  },
  "geometry_checksum": 2448687104.0,
  "bounds": [
    [
      -222.96,
      -12.44
    ],
    [
      814.88,
      582.19
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
