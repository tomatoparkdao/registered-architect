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
    "LINE": 114,
    "LEADER": 4,
    "HATCH": 6,
    "LWPOLYLINE": 11,
    "CIRCLE": 3,
    "ARC": 12,
    "INSERT": 1,
    "TEXT": 8,
    "DIMENSION": 7
  },
  "geometry_checksum": 17772822528.0,
  "bounds": [
    [
      132908.69,
      -27633.65
    ],
    [
      140235.77,
      -21693.07
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
