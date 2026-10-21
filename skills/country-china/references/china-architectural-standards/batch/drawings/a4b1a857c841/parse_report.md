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
    "HATCH": 25,
    "LINE": 911,
    "LWPOLYLINE": 237,
    "ARC": 30,
    "INSERT": 139,
    "CIRCLE": 5,
    "ELLIPSE": 12,
    "TEXT": 110
  },
  "geometry_checksum": -68483084288.0,
  "bounds": [
    [
      -1913.0,
      -16139.63
    ],
    [
      14153.78,
      2580.67
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
