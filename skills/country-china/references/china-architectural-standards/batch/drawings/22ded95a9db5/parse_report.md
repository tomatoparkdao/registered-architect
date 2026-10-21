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
    "LINE": 1324,
    "CIRCLE": 22,
    "LWPOLYLINE": 16,
    "ARC": 22,
    "INSERT": 53,
    "HATCH": 6,
    "SPLINE": 4,
    "TEXT": 124,
    "MTEXT": 19
  },
  "geometry_checksum": 140463538176.0,
  "bounds": [
    [
      2567.78,
      7808.93
    ],
    [
      9489.49,
      11945.94
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
