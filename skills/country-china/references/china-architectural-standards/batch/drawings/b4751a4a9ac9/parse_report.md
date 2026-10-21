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
    "LINE": 36,
    "LWPOLYLINE": 22,
    "HATCH": 12,
    "CIRCLE": 5,
    "TEXT": 62
  },
  "geometry_checksum": 2162093056.0,
  "bounds": [
    [
      -6711.4,
      -10424.31
    ],
    [
      22880.9,
      1097.18
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
