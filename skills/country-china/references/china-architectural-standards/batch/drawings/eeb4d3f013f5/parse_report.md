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
    "LINE": 1251,
    "CIRCLE": 18,
    "LWPOLYLINE": 1256,
    "INSERT": 35,
    "ARC": 4,
    "SOLID": 4,
    "TEXT": 111
  },
  "geometry_checksum": 249236045824.0,
  "bounds": [
    [
      -840.25,
      -1812332.75
    ],
    [
      2278415.25,
      11615.64
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
