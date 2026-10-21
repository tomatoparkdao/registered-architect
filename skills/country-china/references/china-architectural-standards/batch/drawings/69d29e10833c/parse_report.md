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
    "LINE": 15839,
    "ARC": 156,
    "CIRCLE": 24,
    "INSERT": 253,
    "LWPOLYLINE": 11,
    "TEXT": 260,
    "MTEXT": 122
  },
  "geometry_checksum": -5335704141824.0,
  "bounds": [
    [
      -11245.71,
      -6139.97
    ],
    [
      944.56,
      6140.03
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
