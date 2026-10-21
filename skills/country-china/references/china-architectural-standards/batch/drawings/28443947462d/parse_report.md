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
    "LINE": 1948,
    "CIRCLE": 47,
    "ARC": 78,
    "LWPOLYLINE": 680,
    "HATCH": 27,
    "INSERT": 3,
    "TEXT": 588
  },
  "geometry_checksum": 6652071772160.0,
  "bounds": [
    [
      195460.44,
      -104273.92
    ],
    [
      277862.38,
      -16828.26
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
