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
    "CIRCLE": 7,
    "LINE": 139,
    "HATCH": 4,
    "LWPOLYLINE": 2,
    "INSERT": 2,
    "TEXT": 5,
    "MTEXT": 1,
    "DIMENSION": 4
  },
  "geometry_checksum": 1660541696.0,
  "bounds": [
    [
      157882.45,
      -143007.06
    ],
    [
      160239.33,
      -140366.7
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
