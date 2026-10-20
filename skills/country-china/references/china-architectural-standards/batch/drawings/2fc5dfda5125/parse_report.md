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
    "CIRCLE": 15,
    "LINE": 130,
    "ARC": 22,
    "LWPOLYLINE": 10,
    "HATCH": 13,
    "INSERT": 22,
    "TEXT": 1597
  },
  "geometry_checksum": 9428061184.0,
  "bounds": [
    [
      -133.02,
      -183.58
    ],
    [
      2718.58,
      2718.44
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
