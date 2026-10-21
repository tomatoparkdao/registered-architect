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
    "HATCH": 25,
    "LINE": 318,
    "ARC": 20,
    "CIRCLE": 11,
    "INSERT": 36,
    "TEXT": 47
  },
  "geometry_checksum": 71876640768.0,
  "bounds": [
    [
      17118.53,
      -8360.0
    ],
    [
      61180.0,
      23369.86
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
