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
    "LINE": 1542,
    "ARC": 8,
    "CIRCLE": 36,
    "INSERT": 264,
    "LWPOLYLINE": 23,
    "SOLID": 10,
    "POLYLINE": 5,
    "TEXT": 91,
    "MTEXT": 130
  },
  "geometry_checksum": 5332995670016.0,
  "bounds": [
    [
      352701.62,
      -5268.58
    ],
    [
      394751.62,
      24431.42
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
