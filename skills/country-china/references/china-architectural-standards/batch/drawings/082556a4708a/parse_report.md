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
    "LINE": 20,
    "CIRCLE": 3,
    "LWPOLYLINE": 2,
    "TEXT": 4
  },
  "geometry_checksum": -1360005120.0,
  "bounds": [
    [
      -157595.88,
      -359884.81
    ],
    [
      -155084.25,
      -358552.38
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
