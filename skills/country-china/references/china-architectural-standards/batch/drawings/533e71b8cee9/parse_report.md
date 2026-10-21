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
    "LINE": 1965,
    "CIRCLE": 35,
    "ARC": 6,
    "HATCH": 51,
    "SOLID": 7,
    "LWPOLYLINE": 18,
    "INSERT": 194,
    "TEXT": 260,
    "MTEXT": 97
  },
  "geometry_checksum": 941279019008.0,
  "bounds": [
    [
      -9708.46,
      -33453.55
    ],
    [
      96927.66,
      8596.45
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
