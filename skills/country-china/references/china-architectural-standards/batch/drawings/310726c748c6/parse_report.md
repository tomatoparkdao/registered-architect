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
    "LINE": 440,
    "CIRCLE": 5,
    "HATCH": 5,
    "INSERT": 10,
    "LWPOLYLINE": 7,
    "SPLINE": 1,
    "ARC": 10,
    "TEXT": 55,
    "MTEXT": 3
  },
  "geometry_checksum": 18891386880.0,
  "bounds": [
    [
      1572.18,
      10293.4
    ],
    [
      8314.62,
      13997.72
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
