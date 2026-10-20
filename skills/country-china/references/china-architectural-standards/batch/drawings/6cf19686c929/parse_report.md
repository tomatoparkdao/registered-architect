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
    "LINE": 401,
    "CIRCLE": 1,
    "HATCH": 4,
    "ARC": 17,
    "INSERT": 17,
    "LWPOLYLINE": 71,
    "TEXT": 78,
    "MTEXT": 3
  },
  "geometry_checksum": 24443490304.0,
  "bounds": [
    [
      2672.73,
      10471.47
    ],
    [
      12682.28,
      13680.55
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
