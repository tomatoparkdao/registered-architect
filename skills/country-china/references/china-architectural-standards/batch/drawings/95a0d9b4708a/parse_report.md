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
    "INSERT": 6,
    "LINE": 18,
    "LWPOLYLINE": 11,
    "CIRCLE": 1,
    "ARC": 1,
    "TEXT": 1,
    "DIMENSION": 5
  },
  "geometry_checksum": 325768160.0,
  "bounds": [
    [
      -151.19,
      -2255.56
    ],
    [
      20034.74,
      10140.29
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
