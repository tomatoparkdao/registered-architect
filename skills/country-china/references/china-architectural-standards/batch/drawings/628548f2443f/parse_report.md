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
    "LINE": 133,
    "CIRCLE": 4,
    "HATCH": 8,
    "LWPOLYLINE": 5,
    "INSERT": 4,
    "TEXT": 26
  },
  "geometry_checksum": 8120361984.0,
  "bounds": [
    [
      -2957.32,
      9171.69
    ],
    [
      88716.06,
      69281.84
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
