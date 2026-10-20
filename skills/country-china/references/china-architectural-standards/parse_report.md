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
    "LWPOLYLINE": 9,
    "HATCH": 6,
    "CIRCLE": 3,
    "LINE": 9,
    "TEXT": 7,
    "DIMENSION": 5
  },
  "geometry_checksum": 246219424.0,
  "bounds": [
    [
      7699.42,
      11071.94
    ],
    [
      8592.61,
      12200.39
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
