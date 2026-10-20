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
    "LINE": 883,
    "LWPOLYLINE": 114,
    "CIRCLE": 63,
    "INSERT": 21,
    "TEXT": 127,
    "DIMENSION": 132
  },
  "geometry_checksum": 384404488192.0,
  "bounds": [
    [
      -412700.38,
      -18169.57
    ],
    [
      65047.47,
      50306.01
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
