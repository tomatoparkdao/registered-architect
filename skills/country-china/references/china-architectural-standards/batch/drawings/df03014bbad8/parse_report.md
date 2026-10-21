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
    "LINE": 5642,
    "HATCH": 107,
    "SPLINE": 50,
    "LEADER": 6,
    "CIRCLE": 50,
    "INSERT": 1,
    "MTEXT": 2099,
    "TEXT": 58,
    "DIMENSION": 556
  },
  "geometry_checksum": 768918290432.0,
  "bounds": [
    [
      -927.33,
      -2333.14
    ],
    [
      6260.35,
      1383.47
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
