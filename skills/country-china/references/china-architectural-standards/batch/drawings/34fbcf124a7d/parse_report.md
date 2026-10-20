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
    "LWPOLYLINE": 217,
    "LINE": 365,
    "HATCH": 4,
    "ARC": 402,
    "CIRCLE": 18,
    "POLYLINE": 25,
    "MTEXT": 2,
    "TEXT": 1
  },
  "geometry_checksum": 546681389056.0,
  "bounds": [
    [
      8921.47,
      7722.84
    ],
    [
      18004.84,
      23320.15
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
