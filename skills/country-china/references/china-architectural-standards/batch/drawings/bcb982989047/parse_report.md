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
    "LWPOLYLINE": 17,
    "LINE": 78,
    "INSERT": 4,
    "ARC": 2,
    "HATCH": 1,
    "CIRCLE": 1,
    "TEXT": 36,
    "DIMENSION": 16
  },
  "geometry_checksum": 304319872.0,
  "bounds": [
    [
      -134.71,
      -24800.0
    ],
    [
      10053.0,
      3010.49
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
