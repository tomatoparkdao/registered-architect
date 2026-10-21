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
    "LINE": 327,
    "SOLID": 1,
    "CIRCLE": 6,
    "LWPOLYLINE": 39,
    "ARC": 33,
    "POLYLINE": 3,
    "INSERT": 80,
    "TEXT": 83,
    "MTEXT": 2
  },
  "geometry_checksum": 5034815488.0,
  "bounds": [
    [
      -5222.5,
      -164.52
    ],
    [
      3549.56,
      7513.39
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
