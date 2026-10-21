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
    "CIRCLE": 2,
    "LWPOLYLINE": 11,
    "ARC": 2,
    "LINE": 239,
    "INSERT": 2,
    "TEXT": 8,
    "DIMENSION": 3
  },
  "geometry_checksum": 8874771456.0,
  "bounds": [
    [
      18983.75,
      9106.42
    ],
    [
      20398.87,
      10305.74
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
