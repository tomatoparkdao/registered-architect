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
    "LINE": 1180,
    "LEADER": 11,
    "ARC": 36,
    "LWPOLYLINE": 157,
    "INSERT": 2,
    "CIRCLE": 7,
    "HATCH": 11,
    "TEXT": 148,
    "MTEXT": 15,
    "DIMENSION": 53
  },
  "geometry_checksum": 1978620837888.0,
  "bounds": [
    [
      174470.7,
      -26293.64
    ],
    [
      186828.16,
      -18868.64
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
