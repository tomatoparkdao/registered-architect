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
    "LINE": 389,
    "HATCH": 6,
    "LEADER": 7,
    "INSERT": 2,
    "LWPOLYLINE": 2,
    "ARC": 57,
    "MTEXT": 1,
    "TEXT": 10,
    "DIMENSION": 2
  },
  "geometry_checksum": -122870292480.0,
  "bounds": [
    [
      -87864.71,
      -63581.09
    ],
    [
      -85573.32,
      -61376.15
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
