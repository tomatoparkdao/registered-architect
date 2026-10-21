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
    "INSERT": 26,
    "LWPOLYLINE": 1305,
    "LINE": 2451,
    "ARC": 864,
    "CIRCLE": 393,
    "ELLIPSE": 133,
    "SPLINE": 10,
    "HATCH": 1,
    "TEXT": 206,
    "MTEXT": 9,
    "DIMENSION": 205
  },
  "geometry_checksum": -112382394368.0,
  "bounds": [
    [
      -279.95,
      -24.22
    ],
    [
      -247.7,
      -18.66
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
