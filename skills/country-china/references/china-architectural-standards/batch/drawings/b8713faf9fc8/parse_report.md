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
    "LINE": 1584,
    "HATCH": 87,
    "LWPOLYLINE": 234,
    "INSERT": 66,
    "CIRCLE": 38,
    "ARC": 8,
    "POLYLINE": 11,
    "TEXT": 371,
    "DIMENSION": 220
  },
  "geometry_checksum": 4107785732096.0,
  "bounds": [
    [
      -29253.65,
      -71409.41
    ],
    [
      157222.16,
      112674.28
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
