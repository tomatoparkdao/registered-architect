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
    "HATCH": 10,
    "LINE": 1669,
    "CIRCLE": 48,
    "LWPOLYLINE": 16,
    "INSERT": 23,
    "SOLID": 1,
    "TEXT": 37
  },
  "geometry_checksum": 131249504256.0,
  "bounds": [
    [
      -265038.41,
      -336.77
    ],
    [
      39482.7,
      422442.34
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
