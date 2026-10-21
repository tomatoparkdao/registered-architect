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
    "LINE": 279,
    "ARC": 10,
    "HATCH": 7,
    "LWPOLYLINE": 1,
    "CIRCLE": 2,
    "INSERT": 18,
    "TEXT": 33
  },
  "geometry_checksum": 34016970752.0,
  "bounds": [
    [
      11837.75,
      1140.15
    ],
    [
      47778.76,
      81347.03
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
