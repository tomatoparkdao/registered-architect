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
    "LINE": 117,
    "LWPOLYLINE": 47,
    "CIRCLE": 2,
    "HATCH": 3,
    "TEXT": 32
  },
  "geometry_checksum": 76097368.0,
  "bounds": [
    [
      172.47,
      79.58
    ],
    [
      206.3,
      123.58
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
