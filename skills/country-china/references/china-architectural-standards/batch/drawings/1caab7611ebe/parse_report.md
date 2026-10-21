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
    "LINE": 995,
    "SPLINE": 3,
    "LWPOLYLINE": 19,
    "ARC": 22,
    "INSERT": 11,
    "CIRCLE": 30,
    "HATCH": 9,
    "TEXT": 101,
    "MTEXT": 2
  },
  "geometry_checksum": 72960016384.0,
  "bounds": [
    [
      1513.71,
      7882.65
    ],
    [
      8023.01,
      11894.8
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
